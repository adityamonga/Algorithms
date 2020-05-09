from copy import deepcopy

class Board:
    """Game Board"""
    def __init__(self, tiles, moves=0, parent=None):
        self._tiles = tiles
        self.moves = moves
        self.parent = parent

    def toString(self):
        print(self.dimension())
        for row in self._tiles:
            print(" ".join(map(str, row)))

    def dimension(self):
        return len(self._tiles)


    def hamming(self):
        ## returns number of elements which are not in place
        hvalue = 0
        flattened = [inner for outer in self._tiles for inner in outer]
        for pos, value in enumerate(flattened, start=1):
            if value == 0:
                continue
            if pos != value:
                hvalue += 1
        return hvalue

    def manhattan(self):
        mdistance = 0
        flattened = [inner for outer in self._tiles for inner in outer]
        dim = self.dimension()

        for pos, num in enumerate(flattened):
            tiles = deepcopy(flattened)

            if pos == num-1 or num == 0:
                continue

            ## numbers become zero based to match the indices
            num -= 1

            while abs(pos - num) >= dim:
                ## go verticle
                if pos < num:
                    ## go down
                    tiles[pos], tiles[pos+3] = tiles[pos+3], tiles[pos]
                    pos += 3
                    mdistance += 1
                elif num < pos:
                    ## go up
                    tiles[pos], tiles[pos-3] = tiles[pos-3], tiles[pos]
                    pos -= 3
                    mdistance += 1
                else:
                    break

            while 0 < abs(pos - num) < dim:
                ## go horizontal
                if pos < num:
                    ## go right
                    tiles[pos], tiles[pos+1] = tiles[pos+1], tiles[pos]
                    pos += 1
                    mdistance += 1
                elif num < pos:
                    ## go left
                    tiles[pos], tiles[pos-1] = tiles[pos-1], tiles[pos]
                    pos -= 1
                    mdistance += 1
                else:
                    break

        return mdistance

    def isGoal(self):
        flattened = [inner for outer in self._tiles for inner in outer]

        ## In goal state, the last element would be 0
        if flattened[-1] == 0:
            flattened.pop()
        return flattened == sorted(flattened)


    def neighbors(self):
        allneighbors = []
        length = len(self._tiles)

        ## 4*(n^2) extra space in worst case
        for row in range(length):
            for col in range(length):

                if self._tiles[row][col] == 0:
                    if row + 1 < length:
                        tiles = deepcopy(self._tiles)
                        tiles[row][col], tiles[row+1][col]=\
                        tiles[row+1][col], tiles[row][col]

                        allneighbors.append(Board(tiles, self.moves+1, self))

                    if col + 1 < length:
                        tiles = deepcopy(self._tiles)
                        tiles[row][col], tiles[row][col+1]=\
                        tiles[row][col+1], tiles[row][col]

                        allneighbors.append(Board(tiles, self.moves+1, self))

                    if row - 1 > 0:
                        tiles = deepcopy(self._tiles)
                        tiles[row][col], tiles[row-1][col]=\
                        tiles[row-1][col], tiles[row][col]

                        allneighbors.append(Board(tiles, self.moves+1, self))

                    if col - 1 > 0:
                        tiles = deepcopy(self._tiles)
                        tiles[row][col], tiles[row][col-1]=\
                        tiles[row][col-1], tiles[row][col]

                        allneighbors.append(Board(tiles, self.moves+1, self))

        return allneighbors

    @property
    def tiles(self):
        return self._tiles
    
    def __lt__(self, other):
            return (self.moves + self.manhattan()) < (other.moves + other.manhattan())

    def __eq__(self, other):
        return self._tiles == other.tiles

if __name__ == '__main__':
    tiles = [[1,2,3], [4,5,6], [7,8,0]] ## no solution
    tiles = [[0,1,3], [4,2,5], [7,8,6]]
    board = Board(tiles)
    print(board.hamming())
    print(board.manhattan())
    print(board.isGoal())
    # [node.toString() for node in board.neighbors()]
    board.toString()
    neighbors = board.neighbors()
    neighbors[0].toString()
    neighbors[0].parent.toString()

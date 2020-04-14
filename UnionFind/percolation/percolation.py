import os, sys
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from weighted_quick_union import UnionFind

class Percolation:
    """Simulate Percolation to observe state change"""
    def __init__(self, side):
        self.side = side

        ## the first and last elements of list are vitual top and virtual bottom
        ## accessing any element from the list would be 
        ## ( side * (row-1) + col )
        self.uf = UnionFind(side**2 + 2)

        self.track_open = [False for i in range(side**2 + 2)]
        self.track_open[0] = True
        self.open_sites = 0

        ## Opening and connecting virtual sites
        for i in range(1,6):
            ## connect top row to virtual top
            self.uf.union(0,i)
            ## connect bottom row to virtual bottom
            self.uf.union(side**2 + 1, side * (side-1) + i)


    def isOpen(self, row, col):
        return self.track_open[self.getBlockNumber(row, col)] == True

    def open(self, row, col):
        ## for 8 x 8 land; side = 8
        ## row = 3, col = 4; 
        ## block no = 20
        ## neighbours = 19, 21, 28, 12
        if self.isOpen(row, col):
            return

        block_number = self.getBlockNumber(row, col)

        neighbours = [
        (row, col + 1), ## right
        (row, col - 1), ## left
        (row - 1, col), ## up
        (row + 1, col), ## down
        ]
        
        if row == 1:
            neighbours[2] = 0
        elif row == self.side:
            neighbours[-1] = self.side**2 + 1
        if col == 1:
            neighbours.pop(1)
        elif col == self.side:
            neighbours.pop(0)

        for neighbour in neighbours:
            if type(neighbour) is int:
                ## setting nrow and ncol to get virtuals
                if neighbour == 0:
                    nrow, ncol = 1, 0
                else:
                    nrow, ncol = self.side+1, 1 

                block_neighbour = neighbour

            elif type(neighbour) is tuple:
                nrow, ncol = neighbour[0], neighbour[1]
                block_neighbour = self.getBlockNumber(nrow, ncol)

            # print(block_neighbour)
            ## possible bug:: bottom tap is on False until percolated
            ## If condition may fail
            if self.isOpen(nrow, ncol):
                self.uf.union(block_number, block_neighbour)

        self.track_open[block_number] = True
        self.open_sites += 1

    def isFull(self, row, col):
        return self.uf.connected(self.getBlockNumber(row, col), 0)

    def numberOfOpenSites(self):
        return self.open_sites

    def percolates(self):
        percolates = self.uf.connected(0, self.side**2 + 1)
        if percolates:
            self.track_open[-1] = True
            return True
        else:
            return False

    def getBlockNumber(self, row, col):
        # print(row, col)
        return (self.side * (row - 1) + col)        

def display(land):
    print(f"Virtual Top:: {land.uf.data[0]}")
    for index, block in enumerate(land.uf.data[1:-1]):
        if index % land.side == 0:
            print("\n")
        print(block, end ="\t")
    print("\n\nVirtual Bottom:: {}".format(land.uf.data[-1]))
    
    print("\n\n\n")

    print(f"Virtual Top:: {land.track_open[0]}")
    for index, block in enumerate(land.track_open[1:-1]):
        if index % land.side == 0:
            print("\n")
        print(block, end ="\t")
    print("\n\nVirtual Bottom:: {}".format(land.track_open[-1]))
    print("-"*50)

def main(land):
    while not land.percolates():
        i, j = (random.randint(1, land.side) for i in range(2))
        # print(block)
        # breakpoint()
        land.open(i, j)

    # display(land)
    print(f"Number of open sites:: {land.numberOfOpenSites()}")

    threshold = land.numberOfOpenSites() / (land.side**2) * 100
    return threshold

if __name__ == '__main__':
    # land = Percolation(100)
    # print(land.getBlockNumber(7,4))
    simulations = 50
    total_time = 0
    average = 0

    for i in range(simulations):
        land = Percolation(100)
        total_time += main(land)
    average = total_time / simulations
    print(f"Average opened sites for Percolation:: {average}")
    # print(f"Percolates at threshold:: {main(land)}")
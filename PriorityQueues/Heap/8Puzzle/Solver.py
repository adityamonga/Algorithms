from MinHeap import MinHeap
from Board import Board

class Solver:
    """Solver for 8 Puzzle"""
    def __init__(self, board):
        self.board = Board(board, 0, None)
        self.heap = MinHeap()
        self.heap.insert(self.board)
        self.seen = set()

    def exists(self, item):
        ## first element of heap is -sys.maxsize
        return any([True for board in self.heap.heap[1:] if board.tiles == item])

    def solution(self):
        goal = None

        while not goal and not self.heap.isEmpty():
            goal = self.expand()

        if not goal:
            return "No Solution"
            # raise Exception("No Solution")

        path = []
        while goal.parent:
            path.append(goal)
            goal = goal.parent

        path = [self.board] + path[::-1]
        return path

    def expand(self):
        ## find neighbours and proceed with search
        board = self.heap.delMin()
        neighbors = board.neighbors()

        for neighbor in neighbors:
            if neighbor.isGoal():
                return neighbor

            flat = tuple(inner for outer in neighbor.tiles for inner in outer)
            if flat not in self.seen and not self.exists(neighbor.tiles):
                self.heap.insert(neighbor)
                self.seen.add(flat)

    def moves(self):
        path = self.solution()
        ## -1 because it includes original board
        if type(path) is str:
            return path
        return len(path) - 1
        

if __name__ == '__main__':
    s = Solver([[0,1,3], [4,2,5], [7,8,6]])
    r = Solver([[1,2,3], [4,0,5], [6,7,8]])
    print(s.moves())
    print(r.moves())

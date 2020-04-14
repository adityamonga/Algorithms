from collections import deque

class UnionFind():
    """docstring for UnionFind"""
    def __init__(self, size=10):
        self.data = deque([i for i in range(size)], maxlen=size)

    def connected(self, p, q):
        return self.data[p] == self.data[q]

    def union(self, p, q):
        if not self.connected(p, q):
            pid = self.data[p]
            qid = self.data[q]

            for index in range(len(self.data)):
                if self.data[index] == pid:
                    self.data[index] = qid


if __name__ == '__main__':
    uf = UnionFind(10)
    uf.union(1,2)
    uf.union(3,4)
    uf.union(5,6)
    uf.union(0,5)
    uf.union(7,8)
    uf.union(1,9)
    uf.union(2,8)
    print(uf.data)
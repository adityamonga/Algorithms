class UnionFind:
    """docstring for UnionFind"""
    def __init__(self, size):
        self.data = [i for i in range(size)]

    def root(self, node):
        while node != self.data[node]:
            node = self.data[node]
        return node

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)
        self.data[rootp] = rootq

if __name__ == '__main__':
    uf = UnionFind(10)
    print(uf.data)
    print(uf.root(6))
    uf.union(4,3)
    print(uf.data)
    print(uf.connected(4,3))
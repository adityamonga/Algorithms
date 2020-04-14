class UnionFind:
    """docstring for UnionFind"""
    def __init__(self, length):
        self.data = [i for i in range(length)]
        self.size = [0 for i in range(length)]

    def root(self, node):
        while node != self.data[node]:
            ## with path compression 
            ## along the way point every other node to its grandparent
            ## not as efficient as pointing straight to root but just as good
            self.data[node] = self.data[self.data[node]]
            ## just ^ line for path compression
            node = self.data[node]
        return node

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)
        if self.size[rootp] < self.size[rootq]:
            self.data[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.data[rootq] = rootp
            self.size[rootp] += self.size[rootq]

if __name__ == '__main__':
    uf = UnionFind(10)
    print(uf.data)
    print(uf.root(6))
    uf.union(4,3)
    print(uf.data)
    print(uf.connected(4,3))
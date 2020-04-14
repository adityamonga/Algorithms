from weighted_quick_union import UnionFind

class MaxElement(UnionFind):
    """docstring for UnionFind"""
    def __init__(self, length):
        self.max = [i for i in range(length)]
        super().__init__(length)

    def union(self, p, q):
        rootp = self.root(p)
        rootq = self.root(q)

        if self.size[rootp] < self.size[rootq]:
            self.data[rootp] = rootq
            self.size[rootq] += self.size[rootp]
            self.max[rootq] = max(self.max[rootq], self.max[rootq])
        else:
            self.data[rootq] = rootp
            self.size[rootp] += self.size[rootq]
            self.max[rootp] = max(self.max[rootp], self.max[rootq])

    def find(self, element):
        return self.max[self.root(element)]

if __name__ == '__main__':
    m = MaxElement(10)
    m.union(0, 1)
    m.union(6, 7)
    m.union(3, 4)
    m.union(6, 0)
    m.union(2, 5)
    m.union(8, 9)
    m.union(2, 6)
    m.union(3, 6)
    m.union(8, 1)
    print(m.data)
    print(m.max)
    print(m.find(0))
    print(m.find(8))
    # print(m.find(3))
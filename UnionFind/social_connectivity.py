from weighted_quick_union import UnionFind

class SocialConnect:
    """docstring for SocialConnect"""
    def __init__(self, length):
        self.unique_roots = length
        self.uf = UnionFind(length)

    def union(self, p, q, time):
        if not self.uf.root(p) == self.uf.root(q):
            self.unique_roots -= 1
        
        self.uf.union(p, q)
        
        if self.unique_roots == 1:
            return time

        return 0


if __name__ == '__main__':
    s = SocialConnect(10)
    s.union(0, 1, 0.1)
    s.union(6, 7, 0.2)
    s.union(3, 4, 0.3)
    s.union(6, 0, 0.4)
    s.union(2, 5, 0.5)
    s.union(8, 9, 0.6)
    s.union(2, 6, 0.7)
    print(s.union(3, 8, 0.8))
    print(s.union(3, 0, 0.9))
    print(s.unique_roots)

    print(s.uf.data)
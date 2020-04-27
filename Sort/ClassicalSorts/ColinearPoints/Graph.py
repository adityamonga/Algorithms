import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

INFINITY = sys.maxsize
from merge_sort import merge_sort

class Point:
    """Point on a graph"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compareTo(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            if self.x < other.x:
                return True
            else:
                return False
        return False

    def slopeTo(self, other):
        if self.y == other.y:
            return 0

        try:
            slope = (other.y - self.y) / (other.x - self.x)
        except ZeroDivisionError as e:
            if other.y > self.y:
                slope = INFINITY
            else:
                slope = -INFINITY

        return slope

    def slopeOrder(self, p, q):
        return self.slopeTo(p) < self.slopeTo(q)

    def __str__(self):
        return f"({self.x}, {self.y})"

    __repr__ = __str__

    def __lt__(self, other):
        return self.compareTo(other)

class LineSegment:
    """LineSegment with Points"""
    def __init__(self, p: Point, q: Point):
        self.p = p
        self.q = q
        self.slope = self.q.slopeTo(self.p)
        
    def __str__(self):
        return f"{self.p}---{self.q}"

    __repr__ = __str__

    def __lt__(self, other):
        ## point p must be same for both points in this implementation
        return self.p.slopeOrder(self.q, other.q)

if __name__ == '__main__':
    p = Point(1,2)
    q = Point(1,3)
    r = Point(2,3)
    # print(merge_sort([p,q,r]))
    points = [(9, 0), (5, 1), (0, 2), (7, 2), (0, 4), (4, 4), (10, 4), (8, 6), (7, 7), (8, 9)]
    points = [Point(x,y) for x,y in points]
    print(merge_sort(points))
    # print(q<r)
    # print(p.slopeTo(r))
    # print([p,q])
    pq = LineSegment(p,q)
    pr = LineSegment(p,r)
    print(merge_sort([pq, pr]))
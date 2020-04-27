import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import random

from Graph import Point, LineSegment
from merge_sort import merge_sort
from typing import List
from collections import Counter

class FastColinearPoints:
    """Finding Colinear Points on a graph"""
    def __init__(self, points: List):
        self.points = [Point(point[0], point[1]) for point in points]

    def segments(self):
        lines = []
        colinear = set()
        for origin in self.points:
            lines = [LineSegment(origin, point) for point in self.points]

            lines = merge_sort(lines)

            slopes = Counter([line.slope for line in lines])
            mc_slope, mc_count = slopes.most_common(1)[0]

            if mc_count > 3:
                copoints = merge_sort([line.q for line in lines if line.slope == mc_slope])
                colinear.add(tuple(copoints))

            lines = []

        return colinear

if __name__ == '__main__':
    sizex, sizey = 0, 100

    points = [(random.randint(sizex, sizey), random.randint(sizex, sizey))\
    for i in range(50)]
    # points = [(1,1) ,(2,2), (3,3), (4, 4), (7, 7), (8, 9), (0, 2), (7, 2), (9, 0)]
    points = [(19000,10000), (18000,10000), (32000,10000), (21000, 10000), (1234, 5678), (14000,10000)]
    fcp = FastColinearPoints(points)
    for line in fcp.segments():
        print(f"{line[-1]}-->{line[0]}")

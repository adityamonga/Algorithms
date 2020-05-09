import random
import heapq

class DynamicMedian:
    """Heap with priority to median"""
    def __init__(self, collection = None):
        self.minheap = []
        self.maxheap = []
        if collection is not None:
            mid = len(collection) // 2
            collection.sort()
            self.minheap = [-i for i in collection[:mid]]
            self.maxheap = collection[mid:]

            heapq.heapify(self.minheap)
            heapq.heapify(self.maxheap)

    def insert(self, item):
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.minheap, -item)
        else:
            heapq.heappush(self.maxheap, item)

    def isEmpty(self):
        return len(self.minheap) == len(self.maxheap) == 0

    def getMedian(self):
        if len(self.maxheap) > len(self.minheap):
            return heapq.heappop(self.maxheap)
        return -heapq.heappop(self.minheap)


if __name__ == '__main__':
    rlist = random.sample(range(1, 10), 9)
    dm = DynamicMedian(rlist)
    print(dm.minheap)
    print(dm.maxheap)
    while not dm.isEmpty():
        print(dm.getMedian())

from sys import maxsize
import random

class MinHeap:
    """MinHeap Implementation"""
    def __init__(self, collection = None):
        self._heap = [-maxsize]
        self.size = 0
        self.FRONT = 1

        if collection is not None:
            for item in collection:
                self.insert(item)

    def insert(self, item):
        self._heap.append(item)
        self.size += 1
        self.swim(self.size)

    def swim(self, index):
        while index > 1 and self._heap[index] < self._heap[index//2]:
            self.exch(index, index//2)
            index = index//2

    def sink(self, index):
        while 2*index <= self.size:
            child = 2*index
 
            if child + 1 < self.size and self._heap[child + 1] < self._heap[child]:
                child = child+1
 
            if self._heap[index] < self._heap[child]:
                break
            
            self.exch(child, index)
            index = child

    def delMin(self):
        smallest = self._heap[self.FRONT]
        self.exch(self.FRONT, self.size)
        self._heap.pop()
        self.size -= 1
        self.sink(self.FRONT)
        return smallest

    def exch(self, a, b):
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]

    @property    
    def heap(self):
        return self._heap

    def isEmpty(self):
        return self.size == 0

if __name__ == '__main__':
    nums = random.sample(range(50), 20)
    heap = MinHeap(nums)
    print(heap.heap)
    while not heap.isEmpty():
        print(heap.delMin())


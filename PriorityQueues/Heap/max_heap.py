from sys import maxsize as MAXSIZE

class MaxHeap:
    """Max oriented Priority Queue -> Binary Heap"""

    def __init__(self, collection = None):
        self._data = [MAXSIZE]
        self.front = 1
        self.size = 0

        if collection is not None:
            for el in collection:
                self.insert(el)

    @property
    def data(self):
        return self._data

    def isEmpty(self):
        return self.size == 0

    def insert(self, item):
        self._data.append(item)
        self.size += 1
        self.swim(self.size)

    def swim(self, k):
        ## when element at k is greater than parent, swim upwards

        while k > 1 and self._data[k//2] < self._data[k]:
            self.exch(k, k//2)
            k = k//2

    def sink(self, k):
        ## when element at k is smaller than children, sink downwards

        while 2*k <= self.size:
            j = 2*k
            if j + 1 <= self.size and self._data[j] < self._data[j+1]:
                j += 1

            ## we will use 'not <' instead of '>' because 
            ## __lt__() is usually implemented for objects

            if not self._data[k] < self._data[j]:
                break

            self.exch(k, j)
            k = j

    def delMax(self):
        if self.isEmpty():
            return

        max_key = self._data[self.front]
        self.exch(self.front, self.size)
        self._data.pop()
        self.size -= 1
        self.sink(self.front)
        return max_key

    def exch(self, a, b):
        self._data[a], self._data[b] = self._data[b], self._data[a]

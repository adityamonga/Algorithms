from max_heap import MaxHeap
import random

class RandomHeap(MaxHeap):
    """Randomized Operations on MaxHeap"""
    def __init__(self, collection = None):
        super(RandomHeap, self).__init__(collection)

    def sample(self):
        if self.size == 0:
            return 
        return self.data[random.randint(1, self.size)]

    def delRandom(self):
        if self.size == 0:
            return
        r = random.randint(1, self.size)
        rvalue = self._data[r]
        self.exch(r, self.size)
        self._data.pop()
        self.size -= 1
        self.sink(r)
        return rvalue

if __name__ == '__main__':
    rh = RandomHeap()
    print(rh.data)
    for item in random.sample(range(20), 10):
        rh.insert(item)
    print(rh.data)
    print(rh.sample())
    print(rh.delRandom())
    print(rh.data)

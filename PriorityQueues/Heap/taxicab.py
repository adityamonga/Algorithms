import heapq

class Node:
    """Node"""
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.value = (self.a**3) + (self.b**3)
        
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

def makeHeap(n):
    minheap = []
    for index_i in range(1,n):
        for index_j in range(index_i+1, n):
            node = Node(index_i, index_j)
            heapq.heappush(minheap, node)
    return minheap

def taxicab(n):
    minheap = makeHeap(n)
    numbers = set()
    while len(minheap) > 1:
        smallest = heapq.heappop(minheap)
        if smallest.value == minheap[0].value:
            numbers.add((smallest.a, smallest.b, minheap[0].a, minheap[0].b))

    for nums in numbers:
        print(f"{nums[0]}^3 , {nums[1]}^3 = {nums[2]}^3, {nums[3]}^3 = "
        f"{nums[0]**3 + nums[1]**3}")

    return numbers

if __name__ == '__main__':
    taxicab(20)
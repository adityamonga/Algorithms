import stack

class Queue:
    """Queue using two Stacks"""
    def __init__(self):
        self.data = stack.Stack()
        self.reversed = stack.Stack()

    def enqueue(self, value):
        self.data.push(value)

    def dequeue(self):
        while not self.data.isEmpty():
            self.reversed.push(self.data.pop())


        popped = self.reversed.pop()
        
        while not self.reversed.isEmpty():
            self.data.push(self.reversed.pop())        

        return popped

if __name__ == '__main__':
    q = Queue()
    # print(q.data)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.data.isEmpty())
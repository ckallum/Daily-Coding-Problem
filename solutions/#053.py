class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return val

# Fill this in.

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    main()

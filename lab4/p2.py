class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def main():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print("Queue size:", queue.size())
    print("Peek:", queue.peek())
    print("Pop:", queue.pop())
    print("Pop:", queue.pop())

    print("Is queue empty:", queue.is_empty())
    print("Pop:", queue.pop())
    print("Is queue empty:", queue.is_empty())


if __name__ == "__main__":
    main()
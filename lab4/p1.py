class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


def main():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Pop:", stack.pop())

    print("Is stack empty:", stack.is_empty())
    print("Pop:", stack.pop())
    print("Is stack empty:", stack.is_empty())


if __name__ == "__main__":
    main()

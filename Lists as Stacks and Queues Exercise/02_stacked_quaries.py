class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def get_max(self):
        if not self.is_empty():
            return max(self.items)
        else:
            return None

    def get_min(self):
        if not self.is_empty():
            return min(self.items)
        else:
            return None

if __name__ == "__main__":
    stack = Stack()
    N = int(input())
    for _ in range(N):
        query = input().split()
        if query[0] == '1':
            stack.push(int(query[1]))
        elif query[0] == '2':
            stack.pop()
        elif query[0] == '3':
            print(stack.get_max())
        elif query[0] == '4':
            print(stack.get_min())

    # Print the stack from top to bottom
    print(", ".join(map(str, reversed(stack.items))))

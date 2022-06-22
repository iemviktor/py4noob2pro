class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push(self, operation):
        self.stack.append(operation)

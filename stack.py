# A stack is a Last-In-First-Out operational container (LIFO)
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return self.container == 0

    def size(self):
        return len(self.container)


s = Stack()
s.push("1")
s.push("2")
s.push("3")
s.push("4")
s.push("5")

print(s.is_empty())

s.pop()

print(s.peek())
print(s.size())
print(s.container)

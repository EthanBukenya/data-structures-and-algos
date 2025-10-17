from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.appendleft(val)

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0


s = Queue()

s.push({
    'company': 'walmart',
    'timestamp': '5:00 AM',
    'price': 370
})
s.push({
    'company': 'Nilestack',
    'timestamp': '5:02 AM',
    'price': 377
})

print(s.is_empty())
s.pop()
print(s.container)

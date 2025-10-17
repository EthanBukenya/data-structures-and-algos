# Data structure tutorial exercise: Stack
# 1:  Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"


# 2: Write a function in python that checks if paranthesis in the string are balanced or not . Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
'''
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
'''
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


def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    revstr = ''
    while stack.size() != 0:
        revstr += stack.pop()

    return revstr


s = Stack()
s.push("1")
s.push("2")
s.push("3")
s.push("4")
s.push("5")


print(s.peek())
print(s.size())
# print(s[::-1])
print(reverse_string('hey you'))

hello = "Hello"
reverse_hello = hello[::-1]

print(reverse_hello)

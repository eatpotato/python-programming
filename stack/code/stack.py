#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Pystack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def empty(self):
        self.top = -1
        self.stack = []

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top = self.size - 1:
            return True
        else:
            return False

    def push(self, element):
        if self.isFull():
            raise StackException('Pystack is full')
        else:
            self.stack.append(element)
            self.top = self.top + 1

    def pop(self):
        if self.isEmpty():
            raise StackException('Pystack is empty')
        else:
            tmp = self.stack.pop()
            self.top = self.top - 1
            return tmp


class StackException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

if __name__ == '__main__':
    stack = Pystack(20)
    for i in range(1, 10):
        stack.push(i)
    for i in range(1, 10):
        print stack.pop()

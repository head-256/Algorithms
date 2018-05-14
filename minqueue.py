#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stack import Stack


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, data):
        if self.stack.is_empty():
            self.stack.push(data)
            self.min_stack.push(data)
        else:
            min_data = self.min_stack.peek()
            if min_data < data:
                self.min_stack.push(min_data)
            else:
                self.min_stack.push(data)
            self.stack.push(data)

    def pop(self):
        if not self.stack.is_empty():
            self.min_stack.pop()
            return self.stack.pop()

    def get_minimum(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()


class MinQueue:
    def __init__(self):
        self.stack_1 = MinStack()
        self.stack_2 = MinStack()

    def enqueue(self, data):
        self.stack_1.push(data)

    def dequeue(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()

    def get_minimum(self):
        if self.stack_1.is_empty():
            return self.stack_2.get_minimum()
        if self.stack_2.is_empty():
            return self.stack_1.get_minimum()
        return min(self.stack_1.get_minimum(), self.stack_2.get_minimum())


if __name__ == '__main__':
    st = MinStack()
    st.push(5)
    st.push(11)
    st.push(15)
    st.push(3)
    st.push(8)
    print(st.get_minimum())

    q = MinQueue()
    q.enqueue(1)
    q.enqueue(7)
    q.enqueue(3)
    q.enqueue(8)
    q.enqueue(2)
    q.enqueue(77)
    print(q.get_minimum())

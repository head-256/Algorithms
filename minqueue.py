#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stack import Stack


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

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


if __name__ == '__main__':
    st = MinStack()
    st.push(5)
    st.push(11)
    st.push(15)
    st.push(3)
    st.push(8)
    print(st.get_minimum())

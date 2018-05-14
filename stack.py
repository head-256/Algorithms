#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        return self.head.data


if __name__ == '__main__':
    st = Stack()
    st.push(4)
    st.push(7)
    st.push(11)
    st.push(51)
    st.push(2)
    print(st.pop())
    print(st.pop())
    print(st.peek())

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if not self.rear:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front:
            temp = self.front.data
            self.front = self.front.next
            return temp


if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(1)
    print(q.dequeue())

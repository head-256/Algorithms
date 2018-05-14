#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            self.insert_before(self.head, node.data)
        return node

    def append(self, data):
        node = Node(data)
        if not self.tail:
            self.push(node.data)
        else:
            self.insert_after(self.tail, node.data)
        return node

    def insert_after(self, prev_node, data):
        node = Node(data)
        node.prev = prev_node
        if not prev_node.next:
            self.tail = node
        else:
            node.next = prev_node.next
            prev_node.next.prev = node
        prev_node.next = node
        return node

    def insert_before(self, next_node, data):
        node = Node(data)
        node.next = next_node
        if not next_node.prev:
            self.head = node
        else:
            node.prev = next_node.prev
            next_node.prev.next = node
        next_node.prev = node
        return node

    def remove(self, node):
        if not node.prev:
            self.head = node.next
        else:
            node.prev.next = node.next
        if not node.next:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def print_forwards(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


if __name__ == '__main__':
    dll = DoublyLinkedList()
    a = dll.push(3)
    dll.push(7)
    dll.push(42)
    dll.push(13)
    dll.append(5)
    dll.append(9)
    dll.insert_after(dll.head.next, 11)
    b = dll.insert_after(a, 356)
    dll.insert_before(b, 333)
    dll.print_forwards()
    dll.remove(dll.tail)
    print(dll.search(13))
    dll2 = DoublyLinkedList()
    dll2.append(2)
    dll2.print_forwards()

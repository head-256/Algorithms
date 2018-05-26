#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, degree, is_leaf):
        self.degree = degree
        self.is_leaf = is_leaf
        self.keys = [None] * (degree - 1)
        self.childs = [None] * degree
        self.n = 0

    def traverse(self):
        for i in range(self.n):
            if not self.is_leaf:
                self.childs[i].traverse()
            print(' ' + str(self.keys[i]))
            j = i

        if not self.is_leaf:
            self.childs[j].traverse()

    def insert_non_full(self, key):
        i = self.n - 1
        if self.is_leaf:
            while i >= 0 and self.keys[i] > key:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
            self.n += 1
        else:
            while i >= 0 and self.keys[i] > key:
                i -= 1

            if self.childs[i + 1].n == self.degree - 1:
                self.split(i + 1, self.childs[i + 1])
                if self.keys[i + 1] < key:
                    i += 1

            self.childs[i + 1].insert_non_full(key)

    def split(self, i, child):
        node = Node(child.degree, child.is_leaf)
        node.n = self.degree - 1

        for j in range(self.degree - 1):
            node.keys[j] = child.keys[j + self.degree]

        if not child.is_leaf:
            for j in range(self.degree):
                node.childs[j] = child.childs[j + self.degree]

        child.n = self.degree - 1

        for j in range(self.n, i + 1, -1):
            self.childs[j + 1] = self.childs[j]
        self.childs[i + 1] = node

        for j in range(self.n - 1, i, -1):
            self.keys[j + 1] = self.keys[j]
        self.keys[i] = child.keys[self.degree - 1]
        self.n += 1


class BTree:
    def __init__(self, degree):
        self.root = None
        self.degree = degree

    def traverse(self):
        self.root.traverse()

    def insert(self, key):
        if not self.root:
            self.root = Node(self.degree, is_leaf=True)
            self.root.keys[0] = key
            self.root.n = 1
        else:
            if self.root.n == self.degree - 1:
                node = Node(self.degree, is_leaf=False)
                node.childs[0] = self.root
                node.split(0, self.root)

                i = 0
                if node.keys[0] < key:
                    i += 1
                node.childs[i].insert_non_full(key)

                self.root = node
            else:
                self.root.insert_non_full(key)


if __name__ == '__main__':
    t = BTree(4)
    t.insert(3)
    t.insert(1)
    t.insert(5)
    t.insert(4)
    t.insert(2)
    t.insert(9)
    t.insert(10)
    t.insert(8)
    t.insert(7)
    t.insert(6)
    t.traverse()

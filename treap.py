#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, root.priority, end="")
        if root.left:
            print(' :: left child = ' + str(root.left.key), end='')
        if root.right:
            print(' :: right child = ' + str(root.right.key), end='')
        print('\n')
        inorder(root.right)


def _split(t, key):
    if not t:
        return None, None
    elif key > t.key:
        t1, t2 = _split(t.right, key)
        t.right = t1
        return t, t2
    else:
        t1, t2 = _split(t.left, key)
        t.left = t2
        return t1, t


def _merge(t1, t2):
    if not t2:
        return t1
    if not t1:
        return t2

    elif t1.priority > t2.priority:
        t1.right = _merge(t1.right, t2)
        return t1
    else:
        t2.left = _merge(t1, t2.left)
        return t2


class Node:
    def __init__(self, key, priority, left=None, right=None, parent=None):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right
        self.parent = parent


class Treap:
    def __init__(self):
        self.root = None

    @staticmethod
    def _merge(t1, t2):
        return _merge(t1, t2)

    def _split(self, x):
        return _split(self.root, x)

    def insert(self, key):
        t1, t2 = self._split(key)
        m = Node(key, randint(0, 100))
        self.root = self._merge(self._merge(t1, m), t2)

    def remove(self, key):
        t1, t2 = self._split(key - 1)
        m, t2 = self._split(key)
        self.root = self._merge(t1, t2)

    def build(self, keys, priorities):
        tree = Node(keys[0], priorities[0])
        last = tree

        for i in range(1, len(keys)):
            if last.priority > priorities[i]:
                last.right = Node(keys[i], priorities[i], parent=last)
                last = last.right
            else:
                current = last
                while current.parent and current.priority <= priorities[i]:
                    current = current.parent
                if current.priority <= priorities[i]:
                    last = Node(keys[i], priorities[i], left=current)
                else:
                    last = Node(keys[i], priorities[i], left=current.right, parent=current)
                    current.right = last

        while last.parent:
            last = last.parent
        self.root = last


if __name__ == '__main__':
    th = Treap()
    ps = [randint(0, 100) for x in range(7)]
    th.insert(50)
    th.insert(30)
    th.insert(20)
    th.insert(40)
    th.insert(70)
    th.insert(60)
    th.insert(80)
    # print(ps)
    # th.build([1, 2, 3, 4, 5, 6, 7], ps)
    inorder(th.root)

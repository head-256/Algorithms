#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = None


def make_set(x):
    x.parent = x
    x.rank = 1


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root.rank > y_root.rank:
        y_root.parent = x_root
    elif x_root.rank < y_root.rank:
        x_root.parent = y_root
    elif x_root.rank == y_root.rank:
        y_root.parent = x_root
        x_root.rank = x_root.rank + 1


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    make_set(n1)
    make_set(n2)
    make_set(n3)
    make_set(n4)
    union(n1, n4)
    union(n4, n3)
    print(find(n3).data)

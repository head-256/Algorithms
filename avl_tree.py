#!/usr/bin/env python
# -*- coding: utf-8 -*-


def preorder(root):
    if root:
        yield root.key

        for l_child in preorder(root.left):
            yield l_child

        for r_child in preorder(root.right):
            yield r_child


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def _height(node):
    if node is None:
        return 0
    return node.height


def _balance(node):
    if node is None:
        return 0
    return _height(node.left) - _height(node.right)


def _right_rotate(node):
    x = node.left
    T2 = x.right
    x.right = node
    node.left = T2

    node.height = max(_height(node.left), _height(node.right)) + 1
    x.height = max(_height(x.left), _height(x.right)) + 1

    return x


def _left_rotate(node):
    x = node.right
    T2 = x.left
    x.left = node
    node.right = T2

    node.height = max(_height(node.left), _height(node.right)) + 1
    x.height = max(_height(x.left), _height(x.right)) + 1

    return x


def _balancing_insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = _balancing_insert(node.left, key)
    elif key > node.key:
        node.right = _balancing_insert(node.right, key)
    else:
        return node

    node.height = max(_height(node.left), _height(node.right)) + 1
    balance = _balance(node)
    if balance > 1 and key < node.left.key:
        return _right_rotate(node)
    if balance < -1 and key > node.right.key:
        return _left_rotate(node)
    if balance > 1 and key > node.left.key:
        node.left = _left_rotate(node.left)
        return _right_rotate(node)
    if balance < -1 and key < node.right.key:
        node.right = _right_rotate(node.right)
        return _left_rotate(node)
    return node


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        self.root = _balancing_insert(self.root, key)
        return node


if __name__ == '__main__':

    """     30
           /  \
         20   40
        /  \     \
       10  25    50"""

    tr = AVLTree()
    tr.insert(10)
    tr.insert(20)
    tr.insert(30)
    tr.insert(40)
    tr.insert(50)
    tr.insert(25)

    print(list(preorder(tr.root)))

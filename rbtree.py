#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from collections import deque


def bst_insert(root, node):
    if root is None:
        return node
    if node.key < root.key:
        root.left = bst_insert(root.left, node)
        root.left.parent = root
    elif node.key > root.key:
        root.right = bst_insert(root.right, node)
        root.right.parent = root
    return root


def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)


def inorder(root):
    if root:
        for l_child in inorder(root.left):
            yield l_child

        yield root.key

        for r_child in inorder(root.right):
            yield r_child


def preorder(root):
    if root:
        yield root.key

        for l_child in inorder(root.left):
            yield l_child

        for r_child in inorder(root.right):
            yield r_child


def postorder(root):
    if root:
        for l_child in inorder(root.left):
            yield l_child

        for r_child in inorder(root.right):
            yield r_child

        yield root.key


def levelorder(root):
    if root:
        q = deque()
        q.append(root)

        while len(q) > 0:
            temp = q.popleft()
            yield temp.key

            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)


class Color(Enum):
    RED = 0
    BLACK = 1


class Node:
    def __init__(self, key):
        self.key = key
        self.color = Color.RED
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        self.root = bst_insert(self.root, node)
        self._fix_tree(node)

    def _fix_tree(self, node):
        while (node != self.root and node.color != Color.BLACK
                and node.parent.color == Color.RED):
            parent = node.parent
            grand_parent = node.parent.parent

            if parent == grand_parent.left:
                uncle = grand_parent.right
                if uncle is not None and uncle.color == Color.RED:
                    grand_parent.color = Color.RED
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent
                else:
                    if node == parent.right:
                        self._left_rotate(parent)
                        node = parent
                        parent = node.parent
                    self._right_rotate(grand_parent)
                    parent.color, grand_parent.color = grand_parent.color, parent.color
                    node = parent
            else:
                uncle = grand_parent.left
                if uncle is not None and uncle.color == Color.RED:
                    grand_parent.color = Color.RED
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grand_parent
                else:
                    if node == parent.left:
                        self._right_rotate(parent)
                        node = parent
                        parent = node.parent
                    self._left_rotate(grand_parent)
                    parent.color, grand_parent.color = grand_parent.color, parent.color
                    node = parent

        self.root.color = Color.BLACK

    def _left_rotate(self, node):
        sibling = node.right
        node.right = sibling.left
        if sibling.right is not None:
            sibling.right.parent = node
        sibling.parent = node.parent
        if node.parent is None:
            self.root = sibling
        else:
            if node == node.parent.left:
                node.parent.left = sibling
            else:
                node.parent.right = sibling
        sibling.left = node
        node.parent = sibling

    def _right_rotate(self, node):
        sibling = node.left
        node.left = sibling.right
        if sibling.right is not None:
            sibling.left.parent = node
        sibling.parent = node.parent
        if node.parent is None:
            self.root = sibling
        else:
            if node == node.parent.left:
                node.parent.left = sibling
            else:
                node.parent.right = sibling
        sibling.right = node
        node.parent = sibling


if __name__ == '__main__':
    tree = RBTree()
    tree.insert(6)
    tree.insert(22)
    tree.insert(27)
    tree.insert(1)
    tree.insert(11)
    tree.insert(15)
    tree.insert(25)
    tree.insert(8)
    tree.insert(17)
    tree.insert(13)
    print(search(tree.root, 11).left)

    in_order = inorder(tree.root)
    pre_order = preorder(tree.root)
    post_order = postorder(tree.root)
    level_order = levelorder(tree.root)

    print(list(in_order))
    print(list(pre_order))
    print(list(post_order))
    print(list(level_order))

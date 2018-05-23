#!/usr/bin/env python
# -*- coding: utf-8 -*-


def inorder(root):
    if root:
        for l_child in inorder(root.left):
            yield l_child

        yield root.key

        for r_child in inorder(root.right):
            yield r_child


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


def bst_delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = bst_delete(root.left, key)
    elif key > root.key:
        root.right = bst_delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp

        temp = _min_value(root.right)
        root.key = temp.key
        root.right = bst_delete(root.right, temp.key)
    return root


def _min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def successor(node):
    if node.right is not None:
        return _min_value(node.right)

    succ = node.parent
    while succ is not None and node == succ.right:
        node = succ
        succ = succ.parent
    return succ


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        self.root = bst_insert(self.root, node)
        return node

    def delete(self, key):
        bst_delete(self.root, key)


if __name__ == '__main__':
    bst = BST()
    bst.insert(5)
    bst.insert(7)
    n1 = bst.insert(3)
    bst.insert(6)
    bst.insert(11)

    print(successor(n1).key)

    """       50
           /     \
          30      70
         /  \    /  \
       20   40  60   80"""

    bst2 = BST()
    bst2.insert(50)
    bst2.insert(30)
    bst2.insert(20)
    bst2.insert(40)
    bst2.insert(70)
    bst2.insert(60)
    bst2.insert(80)
    print(list(inorder(bst2.root)))
    bst2.delete(20)
    print(list(inorder(bst2.root)))
    bst2.delete(30)
    print(list(inorder(bst2.root)))
    bst2.delete(50)
    print(list(inorder(bst2.root)))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_word_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        node = self.root
        for i in range(len(key)):
            index = ord(key[i]) - ord('a')
            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]
        node.is_word_end = True

    def search(self, key):
        node = self.root
        for i in range(len(key)):
            index = ord(key[i]) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node is not None and node.is_word_end


if __name__ == '__main__':
    t = Trie()
    t.insert('the')
    t.insert('a')
    t.insert('there')
    t.insert('answer')
    t.insert('any')
    t.insert('by')
    t.insert('bye')
    t.insert('their')
    print(t.search('the'))
    print(t.search('these'))

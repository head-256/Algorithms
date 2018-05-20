#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, key):
        self.heap_list.append(key)
        self.size += 1
        self._percolate_up(self.size)

    def _percolate_down(self, i):
        while i * 2 <= self.size:
            min_child = self._min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def _min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def extract(self):
        value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self._percolate_down(1)
        return value

    def build(self, h_list):
        i = len(h_list) // 2
        self.size = len(h_list)
        self.heap_list = [0] + h_list[:]
        while i > 0:
            self._percolate_down(i)
            i -= 1


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.build([9, 5, 6, 2, 3])
    bh.insert(56)
    bh.insert(1)

    print(bh.extract())
    print(bh.extract())
    print(bh.extract())
    print(bh.extract())
    print(bh.extract())
    print(bh.extract())
    print(bh.extract())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


class PriorityQueue:
    def __init__(self):
        self.heap_list = [(0, 0)]
        self.size = 0

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, key):
        self.heap_list.append(key)
        self.size += 1
        self._percolate_up(self.size)

    def _percolate_down(self, i):
        while i * 2 <= self.size:
            min_child = self._min_child(i)
            if self.heap_list[i][0] > self.heap_list[min_child][0]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def _min_child(self, i):
        if i * 2 > self.size:
            return -1
        else:
            if i * 2 + 1 > self.size:
                return i * 2
            else:
                if self.heap_list[i * 2][0] < self.heap_list[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def extract(self):
        value = self.heap_list[1][1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self._percolate_down(1)
        return value

    def build(self, h_list):
        self.size = len(h_list)
        self.heap_list = [(0, 0)]
        for i in h_list:
            self.heap_list.append(i)
        i = len(h_list) // 2
        while i > 0:
            self._percolate_down(i)
            i -= 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def decrease_key(self, val, amt):
        done = False
        i = 1
        my_key = 0
        while not done and i <= self.size:
            if self.heap_list[i][1] == val:
                done = True
                my_key = i
            else:
                i += 1
        if my_key > 0:
            self.heap_list[my_key] = (amt, self.heap_list[my_key][1])
            self._percolate_up(my_key)


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def dijkstra(self, src):
        pq = PriorityQueue()
        dist = [math.inf] * self.V
        pq.insert((0, src))
        dist[src] = 0

        while not pq.is_empty():
            u = pq.extract()
            for value, weight in self.adj[u]:
                v = value
                w = weight
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pq.insert((dist[v], v))

        return dist


if __name__ == '__main__':
    g = Graph(9)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    print(g.dijkstra(0))

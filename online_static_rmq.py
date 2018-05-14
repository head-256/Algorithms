#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

lookup = [[]]


class Query:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def preprocess(A):
    global lookup
    n = len(A)
    l = int(n * math.log2(n))

    lookup = [[0]*l for _ in range(l)]

    for i in range(n):
        lookup[i][0] = i

    j = 1
    while (1 << j) <= n:
        i = 0
        while i + (1 << j) - 1 < n:
            if A[lookup[i][j - 1]] < A[lookup[i + (1 << (j - 1))][j - 1]]:
                lookup[i][j] = lookup[i][j - 1]
            else:
                lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
            i += 1
        j += 1


def query(A, left, right):
    j = int(math.log2(right - left + 1))

    if A[lookup[left][j]] <= A[lookup[right - (1 << j) + 1][j]]:
        return A[lookup[left][j]]
    return A[lookup[right - (1 << j) + 1][j]]


def RMQ(A, Q):
    n = len(Q)
    preprocess(A)

    for i in range(n):
        left = Q[i].left
        right = Q[i].right
        print('[' + str(left) + ', ' + str(right) + ']' + ': ' + str(query(A, left, right)))


if __name__ == '__main__':
    A = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    Q = [Query(0, 4), Query(4, 5), Query(5, 8)]
    RMQ(A, Q)

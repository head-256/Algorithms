#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

A = []
B = []
block_size = 0


def update(index, value):
    global block_size
    global A
    global B

    block_number = int(index / block_size)
    B[block_number] += value - A[index]


def preprocess(I):
    global block_size
    global A
    global B

    n = len(I)
    A = [0] * n
    block_size = int(math.sqrt(n))
    B = [0] * (block_size + 2)
    for j in range(block_size):
        i = j * block_size
        B[j] = i
        while (i + 1) % block_size:
            if I[B[j]] > I[i + 1]:
                B[j] = i + 1
            i += 1
    print(B)


def query(left, right):
    global block_size
    global A
    global B

    sum = 0
    while left < right and left % block_size != 0 and left != 0:
        sum += I[left]
        left += 1
    while left + block_size <= right:
        sum += B[int(left / block_size)]
        left += block_size
    while left <= right:
        sum += I[left]
        left += 1
    return sum


if __name__ == '__main__':
    I = [7, 2, 3, 0, 5, 10, 3, 12, 18, 11, 15, 7]

    preprocess(I)

    print(query(3, 8))
    print(query(1, 4))
    update(1, 0)
    print(query(8, 8))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def build(range_len, A):
    n = len(A)
    B = C = [None] * n
    B[0] = A[0]
    C[-1] = A[-1]
    range_len -= 1

    i1 = 1
    i2 = n - 2
    while i1 < n:
        B[i1] = min(A[i1], B[i1 - 1]) if i1 % range_len else A[i1]
        C[i2] = min(A[i2], C[i2 + 1]) if (i2 + 1) % range_len else A[i2]
        i1 += 1
        i2 -= 1
    return B, C


def get_min(B, C, start, range_len):
    return min(C[start], B[start + range_len - 1])


if __name__ == '__main__':
    A = [1, 6, 3, 8, 9, 23, -29, 56, 78, 5, 1, 4, 100]
    range_len = 3
    start = 6
    B, C = build(range_len, A)
    print(get_min(B, C, start, range_len))

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binary_search(a, b, C, eps):
    left = a
    right = b
    while left + eps < right:
        mid = (left + right) / 2
        if f(mid) + eps < C:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def f(x):
    return x ** 3


if __name__ == '__main__':
    print(binary_search(-4, 4, 27, 0.001))

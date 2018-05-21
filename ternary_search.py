#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ternary_search_min(f, left, right, eps):
    while right - left > eps:
        a = (left * 2 + right) / 3
        b = (left + right * 2) / 3
        if f(a) < f(b):
            right = b
        else:
            left = a
    return (left + right) / 2


def ternary_search_max(f, left, right, eps):
    while right - left > eps:
        a = (left * 2 + right) / 3
        b = (left + right * 2) / 3
        if f(a) > f(b):
            right = b
        else:
            left = a
    return (left + right) / 2


def f(x):
    return -x**2 + 5*x - 6


if __name__ == '__main__':
    print(ternary_search_max(f, -10, 10, 0.01))
    # print(ternary_search_min(f, -10, 10, 0.01))

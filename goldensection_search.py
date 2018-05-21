#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

gr = (math.sqrt(5) + 1) / 2


def gss_min(f, left, right, eps):
    while right - left > eps:
        a = right - (right - left) / gr
        b = left + (right - left) / gr
        if f(a) < f(b):
            right = b
        else:
            left = a
    return (left + right) / 2


def gss_max(f, left, right, eps):
    while right - left > eps:
        a = right - (right - left) / gr
        b = left + (right - left) / gr
        if f(a) > f(b):
            right = b
        else:
            left = a
    return (left + right) / 2


def f(x):
    return -x**2 + 5*x - 6


if __name__ == '__main__':
    print(gss_max(f, -10, 10, 0.01))

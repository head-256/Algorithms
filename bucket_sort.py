#!/usr/bin/env python
# -*- coding: utf-8 -*-
from quadratic_sort_algorithms import insertion_sort


def bucket_sort(elements):
    n = len(elements)
    buckets = [[] for _ in range(n)]

    for i in range(n):
        bucket_index = int(n * elements[i])
        buckets[bucket_index].append(elements[i])

    for i in range(n):
        insertion_sort(buckets[i])

    index = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            elements[index] = buckets[i][j]
            index += 1

    return elements


if __name__ == '__main__':
    elements = [0.482, 0.039, 0.24, 0.175, 0.743, 0.333, 0.395, 0.486, 0.234, 0.838]
    print(bucket_sort(elements))

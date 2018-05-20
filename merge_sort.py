#!/usr/bin/env python
# -*- coding: utf-8 -*-


def merge_sort(elements, left, right):
    if left < right:
        m = (left + right) // 2
        merge_sort(elements, left, m)
        merge_sort(elements, m + 1, right)
        merge(elements, left, m, right)
    return elements


def merge(elements, left, m, right):
    n1 = int(m - left + 1)
    n2 = int(right - m)
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = elements[left + i]
    for j in range(n2):
        R[j] = elements[m + 1 + j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            elements[k] = L[i]
            i += 1
        else:
            elements[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        elements[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        elements[k] = R[j]
        j += 1
        k += 1


if __name__ == '__main__':
    elements = [5, 12, 7, 3, 9, 1]
    print(merge_sort(elements, 0, len(elements) - 1))

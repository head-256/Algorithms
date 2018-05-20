#!/usr/bin/env python
# -*- coding: utf-8 -*-


def quicksort(elements, low, high):
    if low < high:
        partition_index = partition(elements, low, high)
        quicksort(elements, low, partition_index - 1)
        quicksort(elements, partition_index + 1, high)
    return elements


def partition(elements, low, high):
    pivot = elements[high]
    i = low - 1
    for j in range(low, high):
        if elements[j] <= pivot:
            i += 1
            elements[i], elements[j] = elements[j], elements[i]
    elements[i + 1], elements[high] = elements[high], elements[i + 1]
    return i + 1


if __name__ == '__main__':
    elements = [5, 12, 7, 3, 9, 1]
    print(quicksort(elements, 0, len(elements) - 1))

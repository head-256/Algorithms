#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(elements):
    n = len(elements)
    for i in range(n):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements


def selection_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if elements[j] < elements[min_index]:
                min_index = j
        if min_index != i:
            elements[i], elements[min_index] = elements[min_index], elements[i]
    return elements


def insertion_sort(elements):
    n = len(elements)
    for i in range(1, n):
        key = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > key:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key
    return elements


if __name__ == '__main__':
    elements = [5, 12, 7, 3, 9, 1]
    print(bubble_sort(elements))
    elements = [5, 12, 7, 3, 9, 1]
    print(selection_sort(elements))
    elements = [5, 12, 7, 3, 9, 1]
    print(insertion_sort(elements))

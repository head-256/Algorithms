#!/usr/bin/env python
# -*- coding: utf-8 -*-


def max_heapify(elements, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and elements[left] > elements[largest]:
        largest = left
    if right < heap_size and elements[right] > elements[largest]:
        largest = right
    if largest != i:
        elements[i], elements[largest] = elements[largest], elements[i]
        max_heapify(elements, heap_size, largest)


def build_heap(elements):
    heap_size = len(elements)
    for i in range(heap_size // 2, -1, -1):
        max_heapify(elements, heap_size, i)


def heapsort(elements):
    heap_size = len(elements)
    build_heap(elements)
    for i in range(heap_size - 1, 0, -1):
        elements[0], elements[i] = elements[i], elements[0]
        heap_size -= 1
        max_heapify(elements, heap_size, 0)
    return elements


if __name__ == '__main__':
    elements = [5, 12, 7, 3, 9, 1]
    print(heapsort(elements))

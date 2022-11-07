"""
Find the median in the infinite stream of data
"""
from collections import deque
from typing import Deque


def heapify(heap: Deque, parent, end, func):
    while 2 * parent + 1 < end:
        # check for right child
        if 2 * parent + 2 < end:
            x = func(heap[parent], heap[2 * parent + 1], heap[2 * parent + 2])
        else:
            x = func(heap[parent], heap[2 * parent + 1])

        if heap[parent] == x:
            break
        elif heap[2 * parent + 1] == x:
            heap[parent], heap[2 * parent + 1] = heap[2 * parent + 1], heap[parent]
            parent = 2 * parent + 1
        else:
            heap[parent], heap[2 * parent + 2] = heap[2 * parent + 2], heap[parent]
            parent = 2 * parent + 2
    return heap


def extract(heap, func):
    if heap:
        heap[0], heap[-1] = heap[-1], heap[0]
        ele = heap.pop()
        end = len(heap)
        heap = heapify(heap, 0, end, func)
        return ele


def view(heap):
    return heap[0]


def insert(heap: Deque, ele, func):
    heap.appendleft(ele)
    return heapify(heap, 0, len(heap), func)


def stream_median(array):
    min_heap = deque()
    max_heap = deque()
    # for the first element
    max_heap.append(array[0])
    print(view(max_heap))
    for ele in array[1:]:
        # check the entry element
        if view(max_heap) >= ele:
            insert(max_heap, ele, max)
        else:
            insert(min_heap, ele, min)

        if (len(max_heap) - len(min_heap)) > 1:
            temp = extract(max_heap, max)
            insert(min_heap, temp, min)
        elif (len(max_heap) - len(min_heap)) < -1:
            temp = extract(min_heap, min)
            insert(max_heap, temp, max)
        print("max heap ", max_heap)
        print("min heap ", min_heap)
        print("median ", view(max_heap))


if __name__ == '__main__':
    A = [9, 8, 7, 3, 6, 4, 1]
    # Function call
    stream_median(A)

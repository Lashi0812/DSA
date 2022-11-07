from typing import List


def insert(heap, element):
    # insert at last
    heap.append(element)
    # index of parent and child
    child = len(heap) - 1
    parent = (child - 1) >> 1
    # check for the condition
    while heap[child] <= heap[parent]:
        print(heap[parent], heap[child])
        # swap the parent and child
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = (child - 1) >> 1
    return heap


def extract_min(heap: List):
    if heap:
        # swap first and last
        heap[0], heap[-1] = heap[-1], heap[0]
        # get the minimum
        mini = heap.pop()
        # check for parent and child are in right order
        n = len(heap)
        parent = 0
        while (2 * parent + 1) < n:
            # check for right child
            if (2 * parent + 2) < n:
                x = min(heap[parent], heap[2 * parent + 1], heap[2 * parent + 2])
            else:
                x = min(heap[parent], heap[2 * parent + 1])
            if heap[parent] == x:
                break
            elif heap[2 * parent + 1] == x:
                heap[parent], heap[2 * parent + 1] = heap[2 * parent + 1], heap[parent]
                parent = 2 * parent + 1
            else:
                heap[parent], heap[2 * parent + 2] = heap[2 * parent + 2], heap[parent]
                parent = 2 * parent + 2

        return mini, heap


def build_heap(array):
    n = len(array)
    num_leaves = (n + 1) >> 1
    non_leaf = n - num_leaves
    for i in range(non_leaf - 1, -1, -1):
        print(heapify(array, i))


def heapify(heap, parent):
    n = len(heap)
    while (2 * parent + 1) < n:
        # check for right child
        if (2 * parent + 2) < n:
            x = min(heap[parent], heap[2 * parent + 1], heap[2 * parent + 2])
        else:
            x = min(heap[parent], heap[2 * parent + 1])
        if heap[parent] == x:
            break
        elif heap[2 * parent + 1] == x:
            heap[parent], heap[2 * parent + 1] = heap[2 * parent + 1], heap[parent]
            parent = 2 * parent + 1
        else:
            heap[parent], heap[2 * parent + 2] = heap[2 * parent + 2], heap[parent]
            parent = 2 * parent + 2
    return heap


def main():
    # min_heap = [2, 4, 5, 11, 6, 7, 8, 20, 12]
    # print(insert(min_heap, 3))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    # print(extract_min(min_heap))
    build_heap([12, 20, 8, 7, 6, 11, 5, 4, 2])


if __name__ == '__main__':
    main()

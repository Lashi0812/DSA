def heapify(heap, parent, end, func):
    n = end
    while 2 * parent + 1 < n:
        # check for right child
        if 2 * parent + 2 < n:
            x = func(heap[parent], heap[2 * parent + 1], heap[2 * parent + 2])
        else:
            x = func(heap[parent], heap[2 * parent + 1])

        # check for the heap condition
        if heap[parent] == x:
            break
        elif heap[2 * parent + 1] == x:
            heap[parent], heap[2 * parent + 1] = heap[2 * parent + 1], heap[parent]
            parent = 2 * parent + 1
        else:
            heap[parent], heap[2 * parent + 2] = heap[2 * parent + 2], heap[parent]
            parent = 2 * parent + 2
    return heap


def build_heap(array, func):
    n = len(array)
    num_leaves = (n + 1) >> 1
    non_leaf = n - num_leaves
    for i in range(non_leaf, -1, -1):
        heapify(array, i, n, func)
    return array


def sort(heap, func):
    end = len(heap) - 1
    while end >= 0:
        heap[0], heap[end] = heap[end], heap[0]
        heapify(heap, 0, end, func)
        end = end - 1
    return heap


def main():
    arr = [1, 2, 3, 6, 7, 10, 12, 30, 3, 4, 5, 6, 7, 8, 9]
    max_heap = build_heap(arr, max)
    print(max_heap)
    print(sort(max_heap, max))


if __name__ == '__main__':
    main()

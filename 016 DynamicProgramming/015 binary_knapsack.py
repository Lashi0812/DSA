"""Given with n item and their respective weight and value associative the item , we need fill bag of weight W with
these item and attain the maximum value """

import pprint
from typing import List


def recursive(value, weights, bag_weight):
    total_items = len(value)
    store = [[None] * (bag_weight + 1) for _ in range(total_items + 1)]

    def solve(n, w):
        # base condition
        # 1. either the num of items or weight is 0
        if n == 0 or w == 0:
            return 0

        # check we already solve the problem
        if store[n][w] is not None:
            return store[n][w]

        # solve and store the result
        if w >= weights[n - 1]:
            store[n][w] = max(solve(n - 1, w),  # we don't pick that items
                              solve(n - 1, w - weights[n - 1]) + value[n - 1]  # we pick that items
                              )
        else:
            store[n][w] = solve(n - 1, w)

        return store[n][w]

    ans = solve(total_items, bag_weight)
    # what are items we picked
    i = total_items
    j = bag_weight
    items = []
    while i >= 0 and j >= 0:
        if store[i][j] == store[i - 1][j]:
            i -= 1
        else:
            items.append(i)
            j -= weights[i - 1]
            i -= 1

    print("items we picked", items)
    pprint.pprint(store)
    return ans


def iterative(value, weights, bag_weight):
    n = len(value)
    store: List[List] = [[None] * (bag_weight + 1) for _ in range(n + 1)]

    # initialise
    # 1. when the number of items is zero
    for col in range(bag_weight + 1):
        store[0][col] = 0
    # 2. when the bag_weight is zero
    for row in range(n + 1):
        store[row][0] = 0

    # solve the problem
    for items in range(1, n + 1):
        for weigh in range(1, bag_weight + 1):
            if weigh >= weights[items - 1]:
                store[items][weigh] = max(store[items - 1][weigh],  # dont pick
                                          store[items - 1][weigh - weights[items - 1]] + value[items - 1])  # pick
            else:
                store[items][weigh] = store[items - 1][weigh]
    pprint.pprint(store)

    # what are items we picked
    i = n
    j = bag_weight
    items = []
    while i >= 0 and j >= 0:
        if store[i][j] == store[i - 1][j]:
            i -= 1
        else:
            items.append(i)
            j -= weights[i - 1]
            i -= 1

    print("items we picked", items)

    return store[-1][-1]


if __name__ == '__main__':
    # val = [12, 20, 15, 6, 10]
    # wgt = [3, 6, 5, 2, 4]
    val = [2, 3, 5]
    wgt = [3, 4, 7]
    bag_wgt = 8
    print(recursive(val, wgt, bag_wgt))
    print(iterative(val, wgt, bag_wgt))

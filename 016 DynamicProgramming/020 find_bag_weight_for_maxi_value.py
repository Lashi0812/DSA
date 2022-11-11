import pprint
from typing import List


def recursive(value, weight):
    total_items = len(value)
    max_value = sum(value)
    store = [[None] * (max_value + 1) for _ in range(total_items + 1)]

    def solve(n, v):
        # base condition
        # 1. We have items and we make the max_value
        if n == 0 and v != 0:
            return float("inf")
        # 2. we have to make zero max value, and we have n items
        elif v == 0 and n != 0:
            return 0
        # 3. we have to male zero max value, and we have 0 items
        elif v == 0 and n == 0:
            return 0

        # check we already solved the problem
        if store[n][v] is not None:
            return store[n][v]

        # solve and store the result
        store[n][v] = min(
            solve(n - 1, v),  # dont pick
            solve(n - 1, v - value[n - 1])  # pick
            + weight[n - 1]
        )

        return store[n][v]

    ans = solve(total_items, max_value)
    pprint.pprint(store)

    return ans


def iterative(value, weights):
    total_items = len(value)
    max_value = sum(value)
    store: List = [None] * (max_value + 1)

    # initialise
    # 1. when we have zero item  , and we to make the max value
    for _max_value in range(max_value + 1):
        store[_max_value] = float("inf")
    # 2. when we have to make zero happiness , we have zero item
    store[0] = 0
    print(store)
    for _item in range(total_items):
        for _max_value in range(max_value, 0, -1):
            if _max_value >= value[_item]:
                # print(f"cur maxi value is {_max_value} with item value {value[_item]} and its weights {weights[
                # _item]}")
                store[_max_value] = min(
                    store[_max_value],
                    weights[_item] + store[_max_value - value[_item]]
                )
        print(store)

    # find the maximum happiness we will get for budget oh 7
    i = max_value
    while i >= 0:
        if store[i] <= 7:
            return f"The maximum happiness you will get with budget of 7 is {i}"
        i -= 1


if __name__ == '__main__':
    val = [2, 1, 3]
    wgt = [3, 2, 4]
    print(recursive(val, wgt))
    print(iterative(val, wgt))

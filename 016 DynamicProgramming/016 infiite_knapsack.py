"""Given with n item and their respective weight and value associative the item , we need fill bag of weight W with
these item and attain the maximum value , we can choose item any number of times"""


def recursive(values, weights, bag_weight):
    total_items = len(values)
    store = [[None] * (bag_weight + 1) for _ in range(total_items + 1)]

    def solve(n, w):
        # base conditions
        # 1. either the bag weight or number of items is zero
        if n == 0 or w == 0:
            return 0

        # check we already solved the problem
        if store[n][w] is not None:
            return store[n][w]

        # solve and store the result
        if w >= weights[n - 1]:
            store[n][w] = max(solve(n - 1, w),  # don't include in the bag
                              solve(n, w - weights[n - 1]) + values[n - 1])  # include in the bag
        else:
            store[n][w] = solve(n - 1, w)

        return store[n][w]

    ans = solve(total_items, bag_weight)
    picked = []
    i = total_items
    j = bag_weight
    while i > 0 and j > 0:
        if store[i][j] == store[i - 1][j]:
            i -= 1
        else:
            picked.append(i)
            j -= weights[i - 1]

    print(picked)
    return ans


if __name__ == '__main__':
    val = [2, 3, 5]
    wgt = [3, 4, 7]
    bag_wgt = 15
    print(recursive(val, wgt, bag_wgt))

"""You are given an integer array coins representing coins of different denominations and an integer amt
representing a total amt of money.
"""
import pprint
from typing import List


def recursive(coins, amount):
    total_coins = len(coins)
    store = [[None] * (amount + 1) for _ in range(total_coins + 1)]

    def solve(n, k):

        # base condition
        # 1. When the no coins left but still we need to make change
        if n == 0 and k != 0:
            return 0
        # 2. When we got the change but we still have coins
        elif k == 0 and n != 0:
            return 1
        # 3. when both are zero
        elif k == 0 and n == 0:
            return 1

        # check we already solved the problem
        if store[n][k] is not None:
            return store[n][k]

        # solve the problem and store the result
        if k >= coins[n - 1]:

            store[n][k] = solve(n - 1, k) + solve(n - 1, k - coins[n - 1])
        else:
            store[n][k] = solve(n - 1, k)

        return store[n][k]

    ans = solve(total_coins, amount)
    pprint.pprint(store)
    return ans


def iterative(coins, amount):
    total_coins = len(coins)
    store: List[List] = [[None] * (amount + 1) for _ in range(total_coins + 1)]
    # initialize
    # 1. when we have no coins but still we have to give change
    for _change in range(amount + 1):
        store[0][_change] = 0
    # 2. when the change is zero and we have coins
    for _coins in range(total_coins + 1):
        store[_coins][0] = 1

    # solve the problem
    for n in range(1, total_coins + 1):
        for k in range(1, amount + 1):
            if k >= coins[n - 1]:
                store[n][k] = store[n - 1][k] + store[n - 1][k - coins[n - 1]]
            else:
                store[n][k] = store[n - 1][k]

    print(store)
    return store[-1][-1]


if __name__ == '__main__':
    coin = [7, 4, 9, 6, 10, 13, 11, 14]
    amt = 10
    print(recursive(coin, amt))
    print(iterative(coin, amt))

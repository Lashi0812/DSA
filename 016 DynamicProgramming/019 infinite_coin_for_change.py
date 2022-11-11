"""You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
import pprint
from typing import List


def recursive(coins, amount):
    total_coins = len(coins)
    store = [[None] * (amount + 1) for _ in range(total_coins + 1)]

    def solve(n, k):
        # base condition
        # 1. when we have no coin for to give change
        if n == 0 and k != 0:
            return float("inf")
        # 2. when we have coins, but we have already given the change
        elif k == 0 and n != 0:
            return 0  # we don't need any coins to give change
        # 3. when both are zero
        elif k == 0 and n == 0:
            return 0

        # check we already solved the problem
        if store[n][k] is not None:
            return store[n][k]

        # solve and store the result
        if k >= coins[n - 1]:
            store[n][k] = min(
                solve(n - 1, k),  # dont pick
                solve(n, k - coins[n - 1])  # pick it
                + 1  # count the number of coins picked
            )

        else:
            store[n][k] = solve(n - 1, k)

        return store[n][k]

    ans = solve(total_coins, amount)
    pprint.pprint(store)
    return ans


def iterative(coins, amount):
    n = len(coins)
    store: List[List] = [[None] * (amount + 1) for _ in range(n + 1)]
    # initialise
    # 1. when the coin is exhausted and still we need to give change
    for _change in range(amount + 1):
        store[0][_change] = float("inf")
    # 2. when  we have already given the change, but we have coin we have
    for _coin in range(n + 1):
        store[_coin][0] = 0

    # solve the problem
    for n in range(1, n + 1):
        for k in range(1, amount + 1):
            if k >= coins[n - 1]:
                store[n][k] = min(
                    store[n - 1][k],  # don't pick it
                    store[n][k - coins[n - 1]]  # pick it
                    + 1  # if you picked it increase the count
                )
            else:
                store[n][k] = store[n - 1][k]
    pprint.pprint(store)
    return store[-1][-1]


def iterative_reduced_space(coins, amount):
    store = [float("inf") for _ in range(amount + 1)]
    store[0] = 0

    for _change in range(1, amount + 1):
        for _coin in coins:
            needed = _change - _coin
            if needed >= 0:
                store[_change] = min(store[_change], store[needed] + 1)

    return -1 if store[-1] == float("inf") else store[-1]


if __name__ == '__main__':
    coin = [1, 2, 5]
    amt = 4
    print(recursive(coin, amt))
    print(iterative(coin, amt))
    print(iterative_reduced_space(coin, amt))

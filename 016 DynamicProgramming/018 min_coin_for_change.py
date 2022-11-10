from pprint import pprint


def recursive(coins, amount):
    total_coins = len(coins)
    store = [[None] * (amount + 1) for _ in range(total_coins + 1)]

    def solve(n, k):
        # base condition
        # 1. When the coins are exhaust ana still we need to give change
        if n == 0 and k != 0:
            return n + 100  # not possible to give the change
        # 2. when the change is given and we have extra coins
        elif k == 0 and n != 0:
            return 0  # zero coins is need
        # 3. when both are zero
        elif k == 0 and n == 0:
            return 0

        # check we already solve the problem
        if store[n][k] is not None:
            return store[n][k]

        # solve and store the result
        if k >= coins[n - 1]:
            store[n][k] = min(solve(n - 1, k),
                              solve(n - 1, k - coins[n - 1]) + 1)
        else:
            store[n][k] = solve(n - 1, k)

        return store[n][k]

    ans = solve(total_coins, amount)
    pprint(store)
    return ans


if __name__ == '__main__':
    coin = [7, 4, 9, 6, 10, 13, 11, 14]
    amt = 22
    print(recursive(coin, amt))

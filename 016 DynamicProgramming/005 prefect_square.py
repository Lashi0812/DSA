"""
Find min of perfect square needed to get sum = N
"""


def min_psquare(a):
    store = [-1] * (a + 1)

    def psquare(n):
        # base case
        if n == 0:
            return 0
        # check we already solved the sub-problem
        if store[n] != -1:
            return store[n]
        # initialise
        store[n] = 1
        ans = float("inf")
        for i in range(1, int(n ** 0.5) + 1):
            ans = min(ans, psquare(n - i ** 2))
        # store the sub problem result
        store[n] += ans
        return store[n]

    return psquare(a)


if __name__ == '__main__':
    print(min_psquare(12))

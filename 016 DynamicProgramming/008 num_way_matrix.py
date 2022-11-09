"""
Given the matrix of size m*n , find te number of way that we reach the (m-1,n-1 )from (0,0)
"""


def recursive(m, n):
    store = [[None] * n for _ in range(m)]

    def solve(i, j):
        # base condition
        if i == 0 or j == 0:
            return 1
        # check we have already solved the problem
        if store[i][j] is not None:
            return store[i][j]
        # solve the problem and store the result
        store[i][j] = solve(i - 1, j) + solve(i, j - 1)
        print(store)
        return store[i][j]

    return solve(m - 1, n - 1)


def iterative(m, n):
    def solve(i, j):
        print("entering")
        # initialize
        store = [1] * j
        # solve
        for _ in range(i):
            for col in range(1, j):
                store[col] += store[col - 1]
            print(store)
        return store[-1]

    return solve(m - 1, n)


if __name__ == '__main__':
    print(recursive(4, 4))
    print(iterative(4, 4))

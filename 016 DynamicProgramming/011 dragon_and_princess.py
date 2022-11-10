from typing import List


def recursive(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    store = [[None] * n for _ in range(m)]

    def solve(i, j):
        # base condition
        if i == m - 1 and j == n:
            return 1
        elif j == n or i == m:
            return float("inf")

        # check we already solved problem
        if store[i][j] is not None:
            return store[i][j]

        # solve
        store[i][j] = max(min(solve(i + 1, j), solve(i, j + 1)) - dungeon[i][j], 1)

        return store[i][j]

    ans = solve(0, 0)
    print(store)
    return ans


def iterative(dungeon):
    m, n = len(dungeon) - 1, len(dungeon[0]) - 1
    store: List = [1] * (n + 2)

    # initialise
    for i in range(n, -1, -1):
        store[i] = max(store[i + 1] - dungeon[m][i], 1)

    store[-1] = float("inf")

    for row in range(m - 1, -1, -1):
        for col in range(n, -1, -1):
            store[col] = max(min(store[col + 1], store[col]) - dungeon[row][col], 1)
        print(store)
    return store[0]


if __name__ == '__main__':
    mat = [[0, -3]]

    print(recursive(mat))
    print(iterative(mat))

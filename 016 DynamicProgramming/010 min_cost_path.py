"""
Given the matrix with cost of entering particular cell , we need find min cost path from stat to end
"""


def iterative(cost):
    m, n = len(cost), len(cost[0])
    store = [cost[0][0]]
    # initialize
    for i in range(1, n):
        store.append(store[i - 1] + cost[0][i])

    print(store)

    for row in range(1, m):
        for col in range(n):
            if col == 0:
                store[col] += cost[row][col]
            else:
                store[col] = min(store[col - 1], store[col]) + cost[row][col]
        print(store)
    return store[-1]


def recursive(cost):
    m, n = len(cost), len(cost[0])
    store = [[None] * n for _ in range(m)]

    def solve(i, j):
        # print("trying to solving", i, j)

        # base condition
        if i == 0 and j == -1:
            return 0, [(i, j)]
        elif i == -1 or j == -1:
            return float("inf"), [(i, j)]

        # check the problem is solved
        if store[i][j] is not None:
            # print("already solved", i, j)
            return store[i][j]

        # solve and store
        x = solve(i - 1, j)
        y = solve(i, j - 1)
        mini, mini_path = min(x, y)
        mini_cost = cost[i][j] + mini
        make_copy = mini_path.copy()
        make_copy.append((i, j))

        store[i][j] = mini_cost, make_copy

        return store[i][j]

    ans = solve(m - 1, n - 1)
    # print(store)
    return ans


if __name__ == '__main__':
    cost_mat = [[2, 1, 3, 7, 3],
                [3, 3, 4, 8, 3],
                [0, 5, 1, 2, 1],
                [0, 2, 3, 1, 3],
                [4, 1, 5, 2, 3]]

    # print(iterative(cost_mat))
    print(recursive(cost_mat))

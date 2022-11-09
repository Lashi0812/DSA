"""
Given the maze(m,n) with block , we have to reach the end from the start , count the possible ways

Start  : (0,0)
end   : (m-1,n-1)
"""
from typing import List


def recursive(maze):
    m, n = len(maze), len(maze[0])
    store: List[List] = [[None] * n for _ in range(m)]

    def solve(i: int, j: int, mat):
        # print("trying to solving", i, j)
        # base condition
        if i == 0 and j == 0:
            # print("solved enter", i, j)
            store[i][j] = 1
            return 1
        elif i < 0 or j < 0:
            return 0

        # check it is solved
        if store[i][j] is not None:
            # print("already solved", i, j)
            return store[i][j]

        #  solve and store
        if mat[i][j] == 0:
            # print("blocked", i, j)
            store[i][j] = 0
        else:
            store[i][j] = solve(i - 1, j, mat) + solve(i, j - 1, mat)
            # print("storing", i, j)
        # print(store)
        # print("solved", i, j)
        return store[i][j]

    ans = solve(m - 1, n - 1, maze)
    print(store)
    return ans


def iterative(maze: List[List]):
    # initializing
    store = maze[0].copy()
    m, n = len(maze), len(maze[0])
    print(store)

    def solve(i, j):
        # solve row by row
        for row in range(1, i):
            # iterate the col
            for col in range(j):
                if col == 0:
                    store[col] = store[col] and maze[row][col]
                else:
                    if maze[row][col] == 0:
                        store[col] = 0
                    else:
                        store[col] += store[col - 1]
            print(store)
        return store[-1]

    return solve(m, n)


if __name__ == '__main__':
    matrix = [[1, 1, 1, 1],
              [1, 0, 1, 0],
              [0, 1, 1, 1],
              [1, 0, 1, 1],
              [1, 1, 1, 1]]
    print(recursive(matrix))
    print(iterative(matrix))

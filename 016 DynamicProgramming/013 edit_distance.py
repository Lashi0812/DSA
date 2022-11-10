"""
Given the two string convert the s1 into s2 by three operation insert, delete and replace. Find the minimum cost.
"""
from typing import List


def recursive(s1, s2, insert_cost, deletion_cost, replace_cost):
    m, n = len(s1), len(s2)
    store = [[None] * n for _ in range(m)]

    def solve(i, j):
        print("solving", i, j)
        # base condition
        # 1. both string is empty
        if i == -1 and j == -1:
            return 0
        # 2. s1 is empty and s2 has some character ,then we need to add the those character to the s1
        elif i == -1 and j != -1:
            return insert_cost * (j + 1)
        # 3. if the s2 is empty and s1 has some character then we need to delete the character
        elif j == -1 and i != -1:
            return deletion_cost * (i + 1)

        # check already we solve the problem
        if store[i][j] is not None:
            return store[i][j]

        # solve the problem and store the result
        if s1[i] == s2[j]:
            # go diagonally
            store[i][j] = solve(i - 1, j - 1)
        else:
            store[i][j] = min(insert_cost + solve(i, j - 1),  # insertion
                              deletion_cost + solve(i - 1, j),  # deletion
                              replace_cost + solve(i - 1, j - 1)  # replace
                              )

        return store[i][j]

    ans = solve(m - 1, n - 1)
    print(store)

    return ans


def iterative(s1, s2, insert_cost, delete_cost, replace_cost):
    m, n = len(s1), len(s2)
    store: List[List] = [[None] * (n + 1) for _ in range(m + 1)]
    # initialise
    for col in range(1, n + 1):
        store[0][col] = insert_cost * col
    for row in range(1, m + 1):
        store[row][0] = delete_cost * row
    store[0][0] = 0

    # solve row by row
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                store[i][j] = store[i - 1][j - 1]
            else:
                store[i][j] = min(insert_cost + store[i - 1][j],
                                  delete_cost + store[i][j - 1],
                                  replace_cost + store[i - 1][j - 1])

    print(store)
    return store[-1][-1]


if __name__ == '__main__':
    string1 = "horse"
    string2 = "ros"
    print(recursive(string1, string2, 1, 1, 1))
    print(iterative(string1, string2, 1, 1, 1))

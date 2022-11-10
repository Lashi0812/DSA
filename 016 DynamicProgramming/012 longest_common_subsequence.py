"""
Given two string find the length of the longest common subsequence

string1:  abbcdgf
string2: bacdegf

output = 5
"""
from typing import List


def recursive(s1, s2):
    n, m = len(s1), len(s2)
    store: List[List] = [[None] * m for _ in range(n)]

    def solve(i: int, j: int):

        print("solving", i, j)
        # base condition
        # one of the string is empty then stop
        if i == -1 or j == -1:
            return 0

        # check the problem already solved
        if store[i][j] is not None:
            return store[i][j]

        # solve the problem
        if s1[i] == s2[j]:
            print("storing matching", i, j)
            # go diagonally
            store[i][j] = 1 + solve(i - 1, j - 1)
        else:
            print("storing not matching", i, j)
            # max of up and left
            store[i][j] = max(solve(i - 1, j), solve(i, j - 1))

        return store[i][j]

    ans = solve(n-1, m-1)
    print(store)

    # printing the LCS
    a = m-1
    b = n-1
    lcs = ""
    while a > 0 or b > 0:
        if s1[a] == s2[b]:
            lcs += s2[a]
            a -= 1
            b -= 1
        else:
            if store[a - 1][b] >= store[a][b - 1]:
                a -= 1
            else:
                b -= 1

    print(lcs)

    return ans


def iterative(s1, s2):
    n, m = len(s1), len(s2)
    store: List[List] = [[None] * m for _ in range(n)]
    for i, ch1 in enumerate(s1):
        for j, ch2 in enumerate(s2):
            if ch1 == ch2:
                if i - 1 < 0 or j - 1 < 0:
                    store[i][j] = 1
                else:
                    store[i][j] = 1 + store[i - 1][j - 1]
            else:
                if i - 1 < 0 and j - 1 >= 0:
                    store[i][j] = store[i][j - 1]
                elif j - 1 < 0 and i - 1 >= 0:
                    store[i][j] = store[i - 1][j]
                elif i - 1 < 0 and j - 1 < 0:
                    store[i][j] = 0
                else:
                    store[i][j] = max(store[i - 1][j], store[i][j - 1])

    print(store)
    return store[n - 1][m - 1]


if __name__ == '__main__':
    string1 = "kaiya"
    string2 = "maica"
    print(recursive(string1, string2))
    print(iterative(string1, string2))

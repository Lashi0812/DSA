"""
Given the string and pattern with {*,?} , is the string and pattern match
"""
from typing import List


def recursive(s, p):
    m, n = len(s), len(p)
    store: List[List] = [[None] * n for _ in range(m)]

    def solve(i: int, j: int):
        # base condition
        # 1. both string is empty
        if i == -1 and j == -1:
            return True
        # 2. pattern is empty and string is not empty
        elif j == -1 and i != -1:
            return False
        # 3. string is empty and patter is not empty
        elif i == -1 and j != -1:
            # pattern contains only *
            for ele in p[:j]:
                if ele != "*":
                    return False
            return True

        # check the problem is already solved
        if store[i][j] is not None:
            return store[i][j]

        # solve the problem and store the result
        # 1. last character matches or last character of pattern is ?
        if s[i] == p[j] or p[j] == "?":
            # reduce the string and pattern
            store[i][j] = solve(i - 1, j - 1)
        # 2. last character of pattern is *
        elif p[j] == "*":
            # we can replace with 0 character or replace the last character of string
            store[i][j] = solve(i, j - 1) or solve(i - 1, j)
        else:
            store[i][j] = False

        return store[i][j]

    ans = solve(m - 1, n - 1)
    print(store)

    return ans


if __name__ == '__main__':
    string = "abcd"
    pattern = "**"
    print(recursive(string, pattern))

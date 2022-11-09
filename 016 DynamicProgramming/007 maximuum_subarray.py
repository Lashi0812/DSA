"""
Find the maximum sum of subsequence in a array with one condition you cant pick the adjacent element
"""


def recursive(arr):
    store = [None] * len(arr)

    def solve_maxi_subsequence(index, array):

        # base condition
        if index == 0:
            return max(0, array[0])
        elif index == 1:
            return max(0, array[0], array[1])

        # check we have already solved the problem
        if store[index] is not None:
            return store[index]

        # solve the problem and store the result
        store[index] = max(array[index] + solve_maxi_subsequence(index - 2, array),
                           solve_maxi_subsequence(index - 1, array))

        return store[index]

    return solve_maxi_subsequence(len(arr) - 1, arr)


def iterative(arr):
    def solve(array):
        # initialize
        first = max(0, array[0])
        second = max(0, array[0], array[1])
        # solve the problem
        for ele in array[2:]:
            first, second = second, max(ele + first, second, 0)
        return second

    return solve(arr)


if __name__ == '__main__':
    array1 = [-1, -2, 40, 24]
    print(recursive(array1))
    print(iterative(array1))

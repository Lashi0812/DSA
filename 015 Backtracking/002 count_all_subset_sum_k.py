"""
Find count of subset in array of N which has sum = k
"""


def count(cur_ele, total_ele, sums, k, array):
    if cur_ele == total_ele:
        if sums == k:
            return 1
        else:
            return 0
    sums += array[cur_ele]
    x = count(cur_ele + 1, total_ele, sums, k, array)
    sums -= array[cur_ele]
    y = count(cur_ele + 1, total_ele, sums, k, array)
    return x + y


if __name__ == '__main__':
    array = [5, -2, 9]
    print(count(0, len(array), 0, 7, array))

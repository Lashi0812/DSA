"""
Roll as dice , no of ways in which you can get sum =N
"""


def bottom_up(n):
    store = [1]

    def num_ways(x):
        # base condition
        if x == 0:
            return 1
        for j in range(1, n + 1):
            if j <= 6:
                store.append(sum(store))
            else:
                store.append(sum(store[1:]))
        return store[-1]
    return num_ways(n)


if __name__ == '__main__':
    for i in range(13):
        print(f"{i:2} --> {bottom_up(i)}")

def fibo_dp(n):
    store = [-1] * (n + 1)

    def fibo(x):
        if x <= 1:
            return 1
        # checking sub-problem is already calculated
        if store[x] != -1:
            return store[x]

        # store the sub-problem result
        store[x] = fibo(x - 1) + fibo(x - 2)

        return store[x]

    return fibo(n)


if __name__ == '__main__':
    print(fibo_dp(100))

def fibo(n):
    store = [1, 1]
    for i in range(2, n + 1):
        store.append(store[i - 1] + store[i - 2])
    return store[-1]


if __name__ == '__main__':
    print(fibo(5))


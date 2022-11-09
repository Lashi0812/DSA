def fibo(n):
    a = b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(fibo(5))

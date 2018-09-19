def fib(n, accum2, accum1):
    if n == 0:
        return accum2
    elif n == 1:
        return accum1
    else:
        return fib(n - 1, accum1, accum1 + accum2)


def fib2(n):
    accum2 = 0
    accum1 = 1
    if n == 0:
        return accum2
    elif n == 1:
        return accum1
    while True:
        if n == 0:
            break
        elif n == 1:
            break
        else:
            n = n - 1
            temp = accum2
            accum2 = accum1
            accum1 = accum1 + temp

    return accum1


def main():
    n = 0
    while n < 100000:
        print(n, fib2(n))
        n = n + 1

main()

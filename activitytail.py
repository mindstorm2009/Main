def fib(n, accum1, accum2):
    if n == 0:
        return accum1
    elif n == 1:
        return accum2
    else:
        return fib(n - 1, accum2, accum2 + accum1)


print(fib(40, 0, 1))

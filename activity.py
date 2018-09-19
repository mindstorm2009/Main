def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibl(n):
    result = 0
    while n >= 2:
        result = result + fib(n-1) + fib(n-2)
        n = n-1
        print(result)
def main():
    n = 0
    while n<40:
        print(n, fib(n))
        n= n+1

main()
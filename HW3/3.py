def fib(n):
    f1 = f2 = 1
    i = 0
    while (i < n):
        i += 1
        s = f1 + f2
        f1 = f2
        f2 = s
        print(s)
a = int(input())

fib(a)
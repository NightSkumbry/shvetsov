from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n >= 10000:
        return 1
    if n%2 == 0:
        return f(n+3) + 7
    return f(n+1) - 3


print(f(50)-f(57))

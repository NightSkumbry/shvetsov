from sys import setrecursionlimit
setrecursionlimit(20000)

def f(n):
    if n <= 2:
        return 5
    return f(n-2) + n

print(f(23023))

    
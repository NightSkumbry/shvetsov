import sys
sys.setrecursionlimit(2000)


def f(n):
    if n <= 2:
        return n
    return n + f(n-2)

print(f(2023) + f(2020))









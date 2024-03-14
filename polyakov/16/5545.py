from functools import cache
import sys 
sys.setrecursionlimit(20000)

@cache
def f(n):
    if n < 3:
        return 1
    return f(n-1) + f(n-2)

print((f(1006) - f(1004))/f(1005))





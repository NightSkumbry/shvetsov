from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return f(n-1) + f(n-2)


print(f(47))







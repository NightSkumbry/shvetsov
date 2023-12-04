from functools import lru_cache

@lru_cache(None)
def f(n, stop, s, m):
    if n == stop:
        return m > s
    if n > stop:
        return 0
    g = f(n*2, stop, s, m+1)
    g += f(n*5, stop, s, m+1)
    g += f(n+1, stop, s+1, m)
    return g

print(f(3, 260, 0, 0))
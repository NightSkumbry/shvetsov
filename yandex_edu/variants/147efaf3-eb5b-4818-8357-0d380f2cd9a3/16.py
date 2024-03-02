from functools import cache

@cache
def f(n):
    if n <=0:
        return 0
    if n <= 1:
        return 1
    if n%3 == 0:
        return f(n-1)+f(n-3)
    return f(n-2) + 3*n
    
print(f(65))


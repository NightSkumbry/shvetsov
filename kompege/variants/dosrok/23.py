
def f(n, s):
    if n > s:
        return 0
    if n == s:
        return 1
    return f(n+1, s) + f(n*2, s)


print(f(4, 8) * f(8, 10) * f(10, 15))




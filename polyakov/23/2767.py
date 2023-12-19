
def f(n, s):
    if n == 2:
        return 1
    if n < 2:
        return 0
    g = f(n-1, s) + f(n-3, s)
    if n > 4:
        g += f(n%4, s)
    return g

print(f(22, 2))
    








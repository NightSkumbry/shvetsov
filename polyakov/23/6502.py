

def f(n, stop, c = 6, b37 = False):
    if n == stop:
        return 1
    if n > stop or (n > 37 and not b37) or n in [20, 58]:
        return 0
    g = f(n+3, stop, c, b37 or n == 37) + f(n*3, stop, c, b37 or n == 37)
    if c:
        g += f(n+1, stop, c-1, b37 or n == 37)
    return g


print(f(3, 95))




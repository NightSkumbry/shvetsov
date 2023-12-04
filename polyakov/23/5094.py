
def f(n, stop, c):
    if n == stop:
        return 1
    if n > stop:
        return 0
    g = f(n+3, stop, c)
    if n % 2 == 0:
        g += f(n*2+1, stop, c)
    elif c != 0:
        g += f(n*2, stop, c-1)
    return g
        
print(f(1, 76, 5))



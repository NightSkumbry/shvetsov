
def f(n, stop):
    if n == stop:
        return 1
    if n < stop:
        return 0
    g = f(n-2, stop)
    if n%3 != 0:
        g += f(n-n%3, stop)
    return g

print(f(int('212', 3), int('10', 3)))



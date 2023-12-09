
def f(n, stop):
    if n == stop:
        return 1
    if n > stop or n == 13:
        return 0
    return f(n+1, stop) + f(n*2, stop) + f(n*3, stop)

print(f(3, 8) * f(8, 18))


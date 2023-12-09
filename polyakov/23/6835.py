

def f(n, stop):
    if n == stop:
        return 1
    if n > stop or n == 23:
        return 0
    return f(n+2, stop) + f(n*3, stop) + f(n*5, stop)


print(f(1, 13) * f(13, 75))



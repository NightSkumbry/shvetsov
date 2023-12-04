def f(n, stop):
    if n == stop:
        return 1
    if n < stop or n == 7:
        return 0
    return f(n-1, stop)+f(n-3, stop)+f(n//2, stop)

print(f(19, 10) * f(10, 3))
    







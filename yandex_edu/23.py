
def f(n, limit):
    if limit == 0:
        return 1
    if limit == 1:
        return 1 + (n%2 == 0)
    return f(n+1, limit-1) + f(n+2, limit-1) + f(n*3, limit-1)
    

print(f(4, 3) + f(4, 2) + f(4, 1), f(4, 0))

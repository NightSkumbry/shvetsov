
def f(n, s):
    if n > s or n == 12:
        return 0
    if n == s:
        return 1
    return f(n+1, s) + f(n+2, s) + f(n*2, s)

print(f(2, 9)*f(9, 17))



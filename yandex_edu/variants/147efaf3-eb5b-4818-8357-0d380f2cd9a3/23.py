def f(n, s):
    if n < s:
        return 0
    if n == s:
        return 1
    return f(n-2, s)+ f(n//2, s)


print(f(31, 2))

def f(n, s):
    if n < s:
        return 0
    if n == s:
        return 1
    g = f(n-2, s) + f(n-3, s)
    if n**0.5 == int(n**0.5):
        g += f(int(n**0.5), s)
    return g

print(f(25, 3))






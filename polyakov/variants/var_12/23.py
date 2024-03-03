from functools import cache
@cache
def f(n, s, c=0, flag=False):
    if n > 60 or n == 30 or n == 40 or (n > 20 and (not flag)):
        return 0
    if n == s:
        return 1
    if n == 20:
        flag = True
    
    g = f(n+1, s, 0, flag) + f(n+3, s, 0, flag)
    if c == 0:
        g += f(n*2, s, 1, flag)
    return g

print(f(3, 60))







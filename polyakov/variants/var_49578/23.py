
def f(n, s, t1=None, t2=None, t3=None, t=False):
    if n == s and (t or (t1 + t2 + n) % 11 == 0):
        return 1
    if n > s:
        return 0
    
    t1, t2, t3 = n, t1, t2
    if t3 is not None:
        if (t1 + t2 + t3)%11 == 0:
            t = True
    
    return f(n+2, s, t1, t2, t3, t) + f(n*4, s, t1, t2, t3, t) + f(n*3, s, t1, t2, t3, t)

print(f(1, 600))




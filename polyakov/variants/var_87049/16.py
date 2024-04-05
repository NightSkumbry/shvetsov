

def f(n):
    if n < 9:
        return n//3  + n%3
    return f(n//9) + f(n%9)







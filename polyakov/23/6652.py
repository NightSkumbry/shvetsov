
def f(n, c):
    if c == 0:
        return [n]
    return f(n+2, c-1) + f(n*3, c-1)
    
print(len(set(f(1, 4))))



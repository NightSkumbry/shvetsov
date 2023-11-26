
def f_recursion(a):
    b = a.copy()
    for i in range(len(b)-1):
        if b[i+1] < b[i]:
            c = b[i]
            b[i] = b[i+1]
            b[i+1] = c
    if b == a:
        return b
    return f_recursion(b)


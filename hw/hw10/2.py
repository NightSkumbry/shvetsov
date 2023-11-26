
def f_recursion(n1, n2, m=None):
    if m is None:
        m = max(n1, n2)
    if m%n1 == 0 and m%n2 == 0:
        return m
    return f_recursion(n1, n2, m+1)


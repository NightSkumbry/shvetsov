numbers = {i: k for i, k in enumerate('0123456789ABCDEF')}

def f_recursion(number, system=2):
    n = number
    s = system
    if n == 0:
        return ''
    return f_recursion(n//s, s) + numbers[n%s]




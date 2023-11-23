def f1(n): # factorial
    if n == 1:
        return 1
    return n * f1(n-1)


def f2(a): # sum of list
    if len(a) == 1:
        return a[0]
    return a[0] + f2(a[1:])


def f3(n, k, m=None): # gcd
    if m is None:
        m = min(n, k)
    if n%m == 0 and k%m == 0:
        return m
    return f3(n, k, m-1)


def f4(a): # sorting
    b = a.copy()
    for i in range(len(b)-1):
        if b[i+1] < b[i]:
            c = b[i]
            b[i] = b[i+1]
            b[i+1] = c
    if b == a:
        return b
    return f4(b)


def f5(n, m=None): # is prime
    if m is None:
        m = int(n**0.5)
    if m < 2:
        return True
    if n % m == 0:
        return False
    return f5(n, m-1)


def f6(n): # perestonovki
    a = []
    if len(n) == 1:
        return [n]
    for i in range(len(n)):
        a += list(map(lambda x: n[i]+x, f6(n[:i]+n[i+1:])))
    return list(set(a))


def f7(n, k, m=None): # lcm
    if m is None:
        m = max(n, k)
    if m%n == 0 and m%k == 0:
        return m
    return f7(n, k, m+1)


def f4_sl(n):
    if len(n) == 1:
        return n
    h1 = f4_sl(n[:int(len(n)/2)])
    h2 = f4_sl(n[int(len(n)/2):])
    h = []
    for _ in range(len(n)):
        if h1 and h2:
            if h1[0] < h2[0]:
                h.append(h1.pop(0))
            else:
                h.append(h2.pop(0))
        else:
            h += h1 + h2
            break
    return h

print(f4_sl([3,8,9,1,0,7,2,2,6,2]))


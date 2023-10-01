from math import ceil

def dels(n):
    a = 0
    m = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            a += 1
            a += 1 * (n//i != i)
            m = max(i, n//i, m)
    return a, m

for i in range(ceil(12034679**0.25), ceil(23175822**0.25)):
    if dels(i)[0] == 0:
        print(i**4, i**3)

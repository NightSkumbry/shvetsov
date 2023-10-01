def dels(n):
    a = 0
    m = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            a += 1
            a += 1 * (n//i != i)
            m += n//i
            m += i * (n//i != i)
    return a, m

for i in range(135790, 163229):
    r = dels(i)
    if r[1] > 460000:
        print(*r)

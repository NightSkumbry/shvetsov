
def dels(n):
    m = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            m.add(i)
            m.add(n//i)
    return sorted(list(m))


for i in range(143146, 143216):
    if len(dels(i)) == 6:
        print(*dels(i)[-3:-1])




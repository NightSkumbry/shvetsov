# 123456
def dels(n):
    m = set()
    for i in range(2, 1+int(n**0.5)):
        if n%i == 0:
            m.add(n//i)
            m.add(i)
    return list(m)

a = 0
for i in range(123457, 10000000):
    d = dels(i)
    if len(d) == 4:
        print(i, sum(d))
        a += 1
        if a == 5:
            break


def dels(n):
    a = 0
    m = 0
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            a += 1
            a += 1 * (n//i != i)
            m = max(i, n//i, m)
    return a, m

for i in range(321655, 654322, 2):
    r = dels(i)
    if r[0] > 70:
        print(i, r[1])

        
def dels(n):
    a = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            a += 1
            a += 1 * (n//i != i)
    return a

l = [2, 1]
for i in range(1000):
    l.append(l[i] + l[i+1])
for i, e in enumerate(l):
    if e in range(10**6, 10**9+1) and dels(e) == 0:
        print(i+1, e)

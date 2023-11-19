
def dels(n):
    s = set()
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            j = n // i
            if i % 2 == 0:
                s.add(i)
            if j % 2 == 0:
                s.add(j)
    
    return s

a = 0
for i in range(2, 10**6, 2):
    r = dels(75_000_000 + i)
    if len(r) % 2 == 0:
        print(i, len(r)+1)
        a += 1
    if a == 5:
        break
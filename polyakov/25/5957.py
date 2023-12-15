def dels(n):
    m = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            m.add(i)
            m.add(n//i)
    return len(m), sorted(list(m))

for i in range(int(1000**0.5), 10**5):
    if (t:=str(i**2))[0] == t[1] == t[-1] == t[-2]:
        if dels(i**2)[0] == 117:
            print(i**2, dels(i**2)[1][-2])
    if i**2 > 10**9: break



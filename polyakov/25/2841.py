
def dels(n):
    m = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            m.add(i)
            m.add(n//i)
    return len(m), max(m)


for i in range(int(106732567**0.25), int(152673837**0.25)+2):
    if i**4 in range(106732567, 152673837) and dels(i**4)[0] == 3:
        print(i**4, dels(i**4)[1])
        





def dels(n):
    d = set()
    for i in range(1, 1+int(n**0.5)):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(list(d))
for i in range(123456, 987655):
    if int(i**0.5) != i**0.5:
        continue
    d = dels(i)
    if len(d) == 5:
        print(d[-2], d[-1])
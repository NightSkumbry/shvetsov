
for x in range(1, 100000):
    a = 125**7 - 25**4 + x
    r = []
    while a:
        r.append(a%5)
        a //= 5
    
    if r.count(4) == 15 and r.count(3) == 1 and r.count(1) == 2:
        print(x)
        break








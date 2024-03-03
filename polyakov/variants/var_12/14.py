
for x in range(23):
    r = 0
    for i, e in enumerate([6,9,5,8,3,x,7]):
        r += e*23**i
    for i, e in enumerate([6,3,x,4,1]):
        r += e*23**i
    for i, e in enumerate([7,x,1,6]):
        r += e*23**i

    if r % 22 == 0:
        print(x, r//22)
        break






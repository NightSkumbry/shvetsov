
for x in range(27):
    r = 0
    for i, e in enumerate([1,2,3,x,2,4][::-1]):
        r += e*27**i
    for i, e in enumerate([1,3,5,x,7,8][::-1]):
        r += e*27**i
    if r%26 == 0:
        print(x, r//26)








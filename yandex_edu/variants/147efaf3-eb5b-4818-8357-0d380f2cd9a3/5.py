
ans = 0
for i in range(1,10000):
    n = bin(i)[2:]
    if n.count('1')%2 == 0:
        n = '11'+n
    else:
        n+='00'
    if int(n, 2)>116:
        print(i)
        break



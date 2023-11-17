r = 1000000
ans = 0
for i in range(1, 3000):
    n = bin(i)[2:]
    if i % 3 == 0:
        n += '010'
    else:
        n += bin(i%3*5)[2:]
    if int(n, 2) > 300 and n[-1] == '0':
        if int(n, 2) < r:
            r = int(n, 2)
            ans = i
print(ans)
    
    
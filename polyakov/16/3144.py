def F(n,m):
    if m == 0: 
        d = 1
    else: 
        d = n*F(n, m-1)
    return d

ans = 0
for i in range(2, 1000):
    if i**2 in range(100, 1001):
        ans += 1
        
print(ans)


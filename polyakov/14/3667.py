ans = 0
for o in range(2, 11):
    a = 572
    
    r = []
    while a:
        r.append(a%o)
        a //= o
    
    for i in range(len(r)-1):
        if r[i] == r[i+1]:
            ans += o
            break
            
print(ans)



with open('./files/17-1.txt') as f:
    a = list(map(int, f.read().strip().split()))
    b9 = list(map(lambda x: x%9 == 0, a))
    b83 = list(map(lambda x: x%8 == 3, a))

ans = 0
m = -100000000

for i in range(len(a)-1):
    j = i+1
    if b9[i] + b9[j] == 1:
        if b9[i] and b83[j]:
            ans += 1 
            m = max(m, a[i], a[j])
        elif b9[j] and b83[i]:
            ans += 1 
            m = max(m, a[i], a[j])

print(ans, m)

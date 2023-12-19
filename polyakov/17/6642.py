
with open('./files/17-377.txt') as f:
    a = list(map(int, f.read().strip().split()))
    
m = max(filter(lambda x: x%17 == 0, a))
ans = 0
mans = 0

for i in range(len(a)-1):
    if a[i] + a[i+1] > m:
        ans += 1
        mans = max(mans, a[i] + a[i+1])

print(ans, mans)





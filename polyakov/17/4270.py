with open('./files/17-1.txt') as f:
    a = list(map(int, f.read().strip().split()))
    b = list(map(lambda x: str(x)[-1] == '6' and x % 3 == 0, a))

ans = 0
m = 100000000

for i in range(len(a)-1):
    j = i+1
    if b[i] or b[j]:
        ans+=1
        m = min(m, a[i], a[j])

print(ans, m)

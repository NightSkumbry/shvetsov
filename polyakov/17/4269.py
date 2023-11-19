with open('./files/17-1.txt') as f:
    a = list(map(int, f.read().strip().split()))
    b7 = list(map(lambda x: x%7 == 0, a))
    b17 = list(map(lambda x: x% 17 != 0, a))

ans = 0
b = 10000000

for i in range(len(a)-1):
    j = i+1
    if b7[i] + b17[j] == 2 or b17[i] + b7[j] == 2:
        ans += 1
        b = min(b, a[i]+a[j])

print(ans, b)

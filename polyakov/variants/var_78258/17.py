
with open('./polyakov/variants/var_78258/17.txt') as f:
    a = [int(i) for i in f]

M = min(filter(lambda x: x%43 == 0, a))
# print(M)

ans = 0
ans1 = 0

for i in range(len(a)-1):
    if (a[i] + a[i+1]) % M == 0 or (a[i]%10 == M%10 or a[i+1]%10 == M%10):
        ans += 1
        ans1 = max(ans1, a[i], a[i+1])

print(ans, ans1)













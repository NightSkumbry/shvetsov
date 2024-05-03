
with open('./kompege/variants/dosrok/17.txt') as f:
    a = [int(i) for i in f]

m = max(list(filter(lambda x: x%19==0, a)))

ans = ans1 = 0
for i in range(len(a)-1):
    if any([a[i]>m, a[i+1]>m]):
        ans += 1
        ans1 = max(ans1, a[i]+a[i+1])

print(ans, ans1)



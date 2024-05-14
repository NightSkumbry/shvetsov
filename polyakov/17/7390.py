
with open('./files/17-399.txt') as f:
    a = [int(i) for i in f]


m = min(filter(lambda x: len(str(abs(x))) == 3 and str(abs(x))[0] == '5', a))

ans = ans1 = 0
for i in range(len(a)-1):
    if (a[i]+a[i+1]) % m != 0:
        if sum([str(a[i])[-1] == '4', str(a[i+1])[-1]=='4']) == 1:
            ans += 1
            ans1 = max(ans1, a[i] + a[i+1])

print(ans, ans1)

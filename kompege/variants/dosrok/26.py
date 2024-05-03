
with open('./kompege/variants/dosrok/26.txt') as f:
    N = int(f.readline())
    a = [int(i) for i in f]
# d = 3
d = 8

a.sort(key=lambda x: -x)
ans = 0

m = 10**100
while True:
    b = list(filter(lambda x: x <= m-d, a))
    if b:
        m = b[0]
        a = b
        ans += 1
    else:
        break

print(ans, m)





with open('./files/24-250.txt') as f:
    a = f.read().strip()
# print(a[:100])

c = [-10**7 for i in range(6)]
ci = 0
ans = 10**7
for i, e in enumerate(a):
    if e == '.':
        ans = min(ans, i-c[ci%6]+1)
        c[ci%6] = i
        ci += 1

print(ans)

# 012345678910
# .xxx.xxx.x.
# 00000000888
# 000044444410
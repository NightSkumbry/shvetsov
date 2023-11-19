with open('./files/24-181.txt') as f:
    a = f.read()

c = [0 for i in range(4)]
ci = 0
# 012345678910
# .cc.c.c.cc. 
ans = 0
for i, e in enumerate(a):
    if e == '.':
        ans = max(ans, i-c[ci%4]-1)
        c[ci%4] = i
        ci += 1

print(ans)
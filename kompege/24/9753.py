with open('./files/24_9753.txt') as f:
    a = f.read().strip().lower()

# 01234567890123
# y.y..y..y..y.y
c = [0 for i in range(151)]
ci = 0
ans = 0

for i, e in enumerate(a):
    if e == 'y':
        ans = max(ans, i-c[ci%151]-1)
        c[ci%151] = i
        ci += 1
print(max(ans, len(a)-c[ci%151]-1))
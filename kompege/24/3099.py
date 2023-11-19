from collections import Counter as c
with open('./files/24_3099.txt') as f:
    a = f.read().strip().lower()
b = c(a)
ans = 0
for i in 'abcdefghijklmnopqrstuvwxyz':
    if b[i]%2 != 0:
        ans += 1

print(ans//2)

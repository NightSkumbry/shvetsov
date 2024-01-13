from tqdm import tqdm
from math import ceil

with open('./files/26-s1.txt') as f:
    n, *a = list(map(int, f.read().strip().split()))

ans = 0
ans_m = 0
b = []
for i in tqdm(a):
    if i > 100:
        b.append(i)
    else:
        ans += i

b.sort()
l = 0
r = len(b)-1
for i in tqdm(range(len(b)//2)):
    ans += b[r]
    ans += b[l]*0.9
    ans_m = b[l]
    l += 1
    r -= 1

if l == r:
    ans += b[r]

print(ceil(ans), ans_m)



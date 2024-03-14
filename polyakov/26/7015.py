# from functools import cache
# import sys
# sys.setrecursionlimit(10000)

with open('./files/26-139.txt') as f:
    n, k = map(int, f.readline().split())
    a = [list(map(int, i.split())) for i in f]
ans1 = 0
for i in a:
    if i[1] == k:
        ans1 += 1

km = 1
ans = 0
while km <= k:
    b = sorted(filter(lambda x: x[0] <= km, a), key=lambda x: -x[1])
    km = b[0][1] + 1
    ans += 1

print(n-ans, ans1)


















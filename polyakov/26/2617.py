with open('./files/26.txt') as f:
    s, n, *a = map(int, f.read().strip().split())

a.sort()
i = 0
while s-a[i] >= 0:
    s -= a[i]
    i += 1

s += a[i-1]
print(i, max(filter(lambda x: x <= s, a)))






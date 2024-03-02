
with open('./kompege/variants/25044014/26.txt') as f:
    s, n = map(int, f.readline().split())
    a = [int(i) for i in f]
    a.sort()

i = 0
while s - a[i] > 0:
    s -= a[i]
    i += 1

print(i, max(filter(lambda x: x <= s+a[i-1], a)))




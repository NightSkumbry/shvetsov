
with open('./files/26-6.txt') as f:
    s, n = map(int, f.readline().split())
    a = [int(x) for x in f]
    
a.sort()
i = 0
while s-a[i] >= 0:
    s -= a[i]
    i += 1
s += a[i-1]

print(i, max(filter(lambda x: x <= s, a)))









with open('./files/26-k2.txt') as f:
    n, k, *a = map(int, f.read().strip().split())
a.sort()
a = a[k:-k]
print(a[-1], int(sum(a)/len(a)))








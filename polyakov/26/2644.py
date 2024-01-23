
with open('./files/26-j2.txt') as f:
    n, *a = map(int, f.read().strip().split())
a.sort()

m = a[n//2]
srd = sum(a)/n

print(len(list(filter(lambda x: m >= x >= srd, a))))








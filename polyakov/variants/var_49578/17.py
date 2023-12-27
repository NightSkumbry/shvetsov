
with open('./some_files/var/17-316.txt') as f:
    a = [int(i) for i in f.readlines()]

m = max(a)
a1 = a.copy()
a1.remove(m)
m += max(a1)

p = lambda x, y: sum([x[k] == y[k] for k in range(4)]) == 1

ans = 0
sans = 10**100

for i in range(len(a)-2):
    i1 = str(a[i])
    i2 = str(a[i+1])
    i3 = str(a[i+2])
    try:
        if p(i1, i2) or p(i2, i3) or p(i1, i3):
            if int(i1) + int(i2) + int(i3) < m:
                ans += 1
                sans = min(sans, int(i1) + int(i2) + int(i3))
    except:
        print(i1, i2, i3, i)
        raise

print(ans, sans)



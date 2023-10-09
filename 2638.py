with open('./files/26-k1.txt') as f:
    a = list(map(int, f.read().strip().split()[2:]))
    k = 100
    a.sort()
    a = a[::-1]
b = a[:k]
print(a[k], int(sum(map(lambda x: x*0.2, b))))
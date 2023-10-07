with open('./files/17-2.txt') as f:
    a = list(map(int, f.read().strip().split()))

print(a.count(min(a)), len(a)-a[::-1].index(min(a)))

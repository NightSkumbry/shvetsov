with open('./files/17-2.txt') as f:
    a = list(map(int, f.read().strip().split()))

print(a.count(max(a)), a.index(max(a))+1)


with open('./files/26-141.txt') as f:
    N = int(f.readline())
    a = [list(map(int, i.split())) for i in f]
a.sort(key=lambda x: x[1])

ans = 1
ans_1 = a[0][1]
t = a[0][1]
while h := list(filter(lambda x: x[0] >= t, a)):
    t = h[0][1]
    ans += 1

print(ans, ans_1)




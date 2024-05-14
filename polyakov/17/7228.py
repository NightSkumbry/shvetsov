
with open('./files/17-390.txt') as f:
    a = [int(i) for i in f]

c = list(filter(lambda x: str(abs(x))[-2:] == '38', a))

m = sum(c) / len(c)

ans = ans1 = 0
ans1 = -10**1000

for i in range(len(a)-2):
    k = [a[i], a[i+1], a[i+2]]
    if sum([len(str(abs(l))) == 3 for l in k]) in [3,2]:
        if sum([str(l)[-1] == '3' for l in k]) == 1:
            if all([l<m for l in k]):
                ans += 1
                ans1 = max(ans1, sum(k))


print(ans, ans1)
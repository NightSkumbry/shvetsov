
with open('./files/17-390.txt') as f:
    a = [int(i) for i in f]

c = list(filter(lambda x: len(str(abs(x))) >= 3 and str(abs(x))[-3:] == '151', a))

m = sum(c) / len(c)

ans = ans1 = 0
ans1 = 10**1000

for i in range(len(a)-2):
    k = [a[i], a[i+1], a[i+2]]
    if sum([len(str(abs(l))) == 4 for l in k]) in [1,2]:
        if sum([l%13==0 for l in k]) > sum([l%7==0 for l in k]):
            if all([l>m for l in k]):
                ans += 1
                ans1 = min(ans1, sum(k))


print(ans, ans1)






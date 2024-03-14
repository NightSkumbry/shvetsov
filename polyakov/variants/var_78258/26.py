from tqdm import tqdm
with open('./polyakov/variants/var_78258/26.txt') as f:
    N = int(f.readline())
    a = sorted([list(map(int, i.split())) for i in f], key=lambda x: (x[0], -x[1]))

d = [[] for _ in range(a[-1][0]+1)]

for i in a:
    if not d[i[0]]:
        d[i[0]] = [2] + [0]*(i[1])
    d[i[0]][i[1]] = 1

ans = 0
ans1 = 0

for i in tqdm(range(1,len(d))):
    if all(d):
        continue
    for ind, e in enumerate(d[i][1:], 1):
        if e == 0:
            l = 0
            r = 0
            for di in range(-1, -4, -1):
                if ind+di < 0:
                    break
                if d[i][ind+di] != 1:
                    break
                l += 1
            for di in range(1, 4):
                if ind+di >= len(d[i]):
                    break
                if d[i][ind+di] != 1:
                    break
                r += 1
            if l + r >= 3:
                ans += 1
                ans1 = ind
                break


print(ans, ans1)









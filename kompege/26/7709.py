from tqdm import tqdm

with open('./files/26_7709.txt') as f:
    k, n, *a = f.read().strip().split('\n')
    a = list(map(lambda x: list(map(int, x.split())), a))

r = [[1 for i in range(610)] for i in range(int(k))]

ans = 0
ans_s = []

for i in tqdm(a):
    h = range(i[0], i[1]+1)
    for lind, l in enumerate(r):
        if all([l[j] for j in h]):
            for j in h:
                l[j] = 0
            ans += 1
            ans_s.append(lind)
            break

print(ans, ans_s[-2]+1)
    
                







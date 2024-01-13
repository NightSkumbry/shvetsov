from tqdm import tqdm

with open('./files/26-j1.txt') as f:
    n, *a = list(map(int, f.read().strip().split()))

ans = a.count(50)//2
for i in tqdm(range(1, 50)):
    ans += min(a.count(i), a.count(100-i))

print(ans)





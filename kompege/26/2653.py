from tqdm import tqdm
with open('./files/26_2653.txt') as f:
    k, *a = map(int, f.read().strip().split())
    
c = set(range(1, sum(a)+1))
print(sum(a))
r = set()
for i in tqdm(a):
    # print(ind, '/', k)
    l = set()
    for h in r:
        l.add(h+i)
    r.add(i)
    r |= l

# print(c)
# print(r)
t = sorted(c-r)
print(len(t), t[-1])









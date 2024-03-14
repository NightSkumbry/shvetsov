
with open('./files/26-81.txt') as f:
    n, k = map(int, f.readline().split())
    a = [list(map(int, i.split())) for i in f]

rows1 = {}
rows2 = {}
for i in a:
    if i[0] == 1:
        r = rows1.get(i[1], [0]*6).copy()
        r[i[2]-1] = 1
        rows1[i[1]] = r
    elif i[0] == 2:
        r = rows2.get(i[1], [0]*6).copy()
        r[i[2]-1] = 1
        rows2[i[1]] = r
        
ans = 0
ans1 = 0
for r in rows1.keys():
    if rows1[r] == [1,0,0,0,0,1]:
        ans = max(ans, r)
        ans1 += 1
for r in rows2.keys():
    if rows2[r] == [1,0,0,0,0,1]:
        ans = max(ans, r)
        ans1 += 1

print(ans, ans1)















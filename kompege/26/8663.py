with open('./files/26_8663.txt') as f:
    a = f.read().strip().split('\n')[1:]
    a = list(map(lambda x: list(map(int, x.split())), a))
    rows = {}
    for i in a:
        if i[0] in rows.keys():
            rows[i[0]] = max(rows[i[0]], i[1])
        else:
            rows[i[0]] = i[1]

r = {i: ['0' for _ in range(e+1)] for i, e in rows.items()}

ans_r = 0
ans = 0

for row, p in a:
    r[row][p] = '1'

r = {i: ''.join(e) for i, e in r.items()}

for i, e in r.items():
    if e.find('1000001000001') != -1:
        ans += e.count('1000001000001')
        ans_r = max(ans_r, i)

print(ans_r, ans)
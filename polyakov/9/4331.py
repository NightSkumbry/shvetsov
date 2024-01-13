
with open('./files/9-107.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]


ans = 0
for i in a:
    if i[0] == i[1] == i[2] == 60:
        ans += 1

print(ans)





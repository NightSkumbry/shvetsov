with open('./files/27A_2724.txt') as f:
    a = list(map(int, f.read().strip().split('\n')[1:]))
b = [0 for i in range(131)]
for i in a:
    b[i%131] += 1

ans = 0
for i in a:
    b[i%131] -= 1
    ans += b[(131-i%131)%131]

print(ans)

with open('./files/27B_2724.txt') as f:
    a = list(map(int, f.read().strip().split('\n')[1:]))
b = [0 for i in range(131)]
for i in a:
    b[i%131] += 1

ans = 0
for i in a:
    b[i%131] -= 1
    ans += b[(131-i%131)%131]

print(ans)








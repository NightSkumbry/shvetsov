
with open('./files/24_13715.txt') as f:
    a = f.read().strip().lower().replace('ab', 'a1b')

b = list(map(len, a.split('1')))
ans = 0
for i in range(len(b)):
    ans = max(ans, sum(b[i:i+51]))
print(ans)




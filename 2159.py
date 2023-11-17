with open('./files/2159.txt') as f:
    g = f.read()
    g = '1\n'+'2\n'*1000000+'1'
    a = list(map(int, g.strip().split('\n')))

l = len(a)

nech = list(map(lambda x: x%2, a))

sn = sum(nech)
c = [l-sn, sn]
for i in range(9):
    c[nech[i]] -= 1
ans = 0
for i in range(0, l-9):
    ans += c[1-nech[i]]
    c[nech[i+9]] -= 1

print(c, ans)

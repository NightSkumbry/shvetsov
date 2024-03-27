
with open('./files/26-68.txt') as f:
    N, T = map(int, f.readline().split())
    a = [list(map(int, i.split())) for i in f]
    # T = 50

su = sum(map(lambda x: x[0], a))/len(a)

sv = sorted(map(lambda x: x[1], filter(lambda x: x[0] > su, a)))
nv = sorted(map(lambda x: x[1], filter(lambda x: x[0] <= su, a)))


f = 0
si = 0
ni = 0
ans = ans1 = 0
while ni < len(nv):
    t = T-nv[ni]
    ans += 1
    ni += 1
    if si < len(sv) and t - sv[si] >= 0:
        t -= sv[si]
        ans += 1
        ans1 += sv[si]
        si += 1
    else:
        f = 1
    T = t
    if f:
        break
        
    
print(ans, ans1)
















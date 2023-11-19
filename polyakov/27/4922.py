def A():
    with open('./files/4922_a.txt') as f:
        a = f.read().strip().split('\n')
        d = int(a[0].split()[1])
        a = list(map(int, a[1:]))
    ans = 0
    s = 0
    b = []
    for i in a:
        s += i
        ans += s%d == 0
        for k in b:
            ans += (s-k)%d == 0
        b.append(s)
    print(ans)

A()

def B():
    with open('./files/4922_b.txt') as f:
        a = f.read().strip().split('\n')
        d = int(a[0].split()[1])
        a = list(map(int, a[1:]))
    ans = 0
    s = 0
    b = [0 for i in range(d)]
    for i in a:
        s += i
        ans += s%d == 0
        ans += b[s%d]
        b[s%d] += 1
    print(ans)

B()
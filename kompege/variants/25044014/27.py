def A():
    with open('./kompege/variants/25044014/27-A.txt') as f:
        n, d = map(int, f.readline().split())
        a = [int(i) for i in f]
    a.sort()
    ans = 0
    while a:
        ans += 1
        l = d - a.pop()
        if a[0] <= l:
            a.pop(0)
    print(ans)

def B():
    with open('./kompege/variants/25044014/27-B.txt') as f:
        n, d = map(int, f.readline().split())
        a = [int(i) for i in f]
    a.sort()
    ans = 0
    lh = 0
    r = len(a)-1
    while r >= lh:
        ans += 1
        l = d - a[r]
        r -= 1
        if a[lh] <= l:
            lh += 1
    print(ans)

A()
B()















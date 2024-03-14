from math import ceil


def f19(x,y,t=0):
    if x + y <= 20:
        if t == 2:
            return True
        return False
    if t >= 2:
        return False

    a = [f19(x-1, y, t+1), f19(x, y-1, t+1), f19(ceil(x/2), y, t+1), f19(x, ceil(y/2), t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)


for s in range(11, 1000):
    if f19(10, s):
        print(s)


def f20(x,y,t=0):
    if x + y <= 20:
        if t == 3:
            return True
        return False
    if t >= 3:
        return False

    a = [f20(x-1, y, t+1), f20(x, y-1, t+1), f20(ceil(x/2), y, t+1), f20(x, ceil(y/2), t+1)]
    
    if t%2 == 1:
        return all(a)
    return any(a)


ans = []
for s in range(11, 1000):
    if f20(10, s):
        ans.append(s)
print(ans, ans[0], ans[-1])


def f21(x,y,t=0):
    if x + y <= 20:
        if t in [2,4]:
            return True
        return False
    if t >= 4:
        return False

    a = [f21(x-1, y, t+1), f21(x, y-1, t+1), f21(ceil(x/2), y, t+1), f21(x, ceil(y/2), t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)


for s in range(11, 1000):
    if f21(10, s) and not f19(10,s):
        print(s)


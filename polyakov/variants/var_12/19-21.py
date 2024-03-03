
def f19(x,y,t=0):
    if max(x,y) >= 65:
        if t == 1:
            return True
        return False
    if t >= 1:
        return False
    
    if x > y:
        a = [f19(x+1, y, t+1), f19(x+2, y, t+1), f19(x+3, y, t+1), f19(x, y*2, t+1)]
    if x < y:
        a = [f19(x, y+1, t+1), f19(x, y+2, t+1), f19(x, y+3, t+1), f19(x*2, y, t+1)]
    if x == y:
        a = [f19(x+1, y, t+1), f19(x+2, y, t+1), f19(x+3, y, t+1), f19(x, y+1, t+1), f19(x, y+2, t+1), f19(x, y+3, t+1)]

    if t % 2 == 0:
        return any(a)
    return all(a)

ans = 1110
for x in range(1, 65):
    for y in range(1 ,65):
        if f19(x,y):
            ans = min(ans, x+y)
print(ans)


def f20(x,y,t=0):
    if max(x,y) >= 65:
        if t == 3:
            return True
        return False
    if t >= 3:
        return False
    
    if x > y:
        a = [f20(x+1, y, t+1), f20(x+2, y, t+1), f20(x+3, y, t+1), f20(x, y*2, t+1)]
    if x < y:
        a = [f20(x, y+1, t+1), f20(x, y+2, t+1), f20(x, y+3, t+1), f20(x*2, y, t+1)]
    if x == y:
        a = [f20(x+1, y, t+1), f20(x+2, y, t+1), f20(x+3, y, t+1), f20(x, y+1, t+1), f20(x, y+2, t+1), f20(x, y+3, t+1)]

    if t % 2 == 0:
        return any(a)
    return all(a)

ans = []
for s in range(65):
    if f20(18, s):
        ans.append(s)
print(ans, ans[0], ans[-1])


def f21_dop(x,y,t=0):
    if max(x,y) >= 65:
        if t == 2:
            return True
        return False
    if t >= 2:
        return False
    
    if x > y:
        a = [f21_dop(x+1, y, t+1), f21_dop(x+2, y, t+1), f21_dop(x+3, y, t+1), f21_dop(x, y*2, t+1)]
    if x < y:
        a = [f21_dop(x, y+1, t+1), f21_dop(x, y+2, t+1), f21_dop(x, y+3, t+1), f21_dop(x*2, y, t+1)]
    if x == y:
        a = [f21_dop(x+1, y, t+1), f21_dop(x+2, y, t+1), f21_dop(x+3, y, t+1), f21_dop(x, y+1, t+1), f21_dop(x, y+2, t+1), f21_dop(x, y+3, t+1)]

    if t % 2 == 0:
        return all(a)
    return any(a)


def f21(x,y,t=0):
    if max(x,y) >= 65:
        if t in [2,4]:
            return True
        return False
    if t >= 4:
        return False
    
    if x > y:
        a = [f21(x+1, y, t+1), f21(x+2, y, t+1), f21(x+3, y, t+1), f21(x, y*2, t+1)]
    if x < y:
        a = [f21(x, y+1, t+1), f21(x, y+2, t+1), f21(x, y+3, t+1), f21(x*2, y, t+1)]
    if x == y:
        a = [f21(x+1, y, t+1), f21(x+2, y, t+1), f21(x+3, y, t+1), f21(x, y+1, t+1), f21(x, y+2, t+1), f21(x, y+3, t+1)]

    if t % 2 == 0:
        return all(a)
    return any(a)

for s in range(1, 65):
    if f21(26, s) and not f21_dop(26, s):
        print(s)




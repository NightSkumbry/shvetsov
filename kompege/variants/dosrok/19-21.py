
def f19(x, y, t=0):
    if x+y >= 123:
        if t == 2:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(x+1, y, t+1), f19(x*2, y, t+1), f19(x, y+1, t+1), f19(x, y*2, t+1)]

    return any(a)


def f20(x, y, t=0):
    if x+y >= 123:
        if t == 3:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(x+1, y, t+1), f20(x*2, y, t+1), f20(x, y+1, t+1), f20(x, y*2, t+1)]

    if t%2:
        return all(a)
    return any(a)


def f21_dop(x, y, t=0):
    if x+y >= 123:
        if t == 2:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f21_dop(x+1, y, t+1), f21_dop(x*2, y, t+1), f21_dop(x, y+1, t+1), f21_dop(x, y*2, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)

def f21(x, y, t=0):
    if x+y >= 123:
        if t in [2, 4]:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(x+1, y, t+1), f21(x*2, y, t+1), f21(x, y+1, t+1), f21(x, y*2, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)


for s in range(1, 110):
    if f19(13, s):
        print(s)
        break

ans = []
for s in range(1, 110):
    if f20(13, s):
        ans.append(s)
print(*ans[:2])

for s in range(1, 110):
    if f21(13, s) and not f21_dop(13, s):
        print(s)
        break










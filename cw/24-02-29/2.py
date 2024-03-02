
def f19(x, t=0):
    if x < 117:
        if t == 2:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(x-7, t+1), f19(x//3, t+1)]

    return any(a)

ans = []
for s in range(117, 10_000):
    if f19(s):
        ans.append(s)
print(ans[-1])

def f20(x, t=0):
    if x < 117:
        if t == 3:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(x-7, t+1), f20(x//3, t+1)]

    if t%2 == 0:
        return any(a)
    return all(a)

ans = []
for s in range(117, 10_000):
    if f20(s):
        ans.append(s)
print(ans[0], ans[-1])

def f21_dop(x, t=0):
    if x < 117:
        if t == 2:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f21_dop(x-7, t+1), f21_dop(x//3, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)

def f21(x, t=0):
    if x < 117:
        if t == 2 or t == 4:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(x-7, t+1), f21(x//3, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)


ans = []
for s in range(117, 10_000):
    if f21(s) and not f21_dop(s):
        ans.append(s)
print(ans[-1])


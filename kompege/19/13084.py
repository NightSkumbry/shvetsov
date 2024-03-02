
def f19(s, t=0):
    if s >= 84:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    if s % 2 == 0:
        a = [f19(s+1, t+1), f19(int(s*1.5), t+1)]
    else:
        a = [f19(s+1, t+1), f19(s*2, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)


def f20(s, t=0):
    if s >= 84:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    if s % 2 == 0:
        a = [f20(s+1, t+1), f20(int(s*1.5), t+1)]
    else:
        a = [f20(s+1, t+1), f20(s*2, t+1)]

    if t%2 == 1:
        return all(a)
    return any(a)


def f21(s, t=0):
    if s >= 84:
        if t in [2, 4]:
            return True
        return False
    if t >= 4:
        return False
    
    if s % 2 == 0:
        a = [f21(s+1, t+1), f21(int(s*1.5), t+1)]
    else:
        a = [f21(s+1, t+1), f21(s*2, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)


a = []
for s in range(1, 84):
    if f19(s):
        a.append(s)
print(a[-1])

a = []
for s in range(1, 84):
    if f20(s):
        a.append(s)
print(a[0], a[1])

a = []
for s in range(1, 84):
    if f21(s) and not f19(s):
        a.append(s)
print(a[-1])


def f19b(s, t=0):
    if s <= 116:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f19b(s-7, t+1), f19b(s//3, t+1)]
    
    return any(a)


def f19(s, t=0):
    if s <= 116:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(s-7, t+1), f19(s//3, t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)


def f20(s, t=0):
    if s <= 116:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(s-7, t+1), f20(s//3, t+1)]
    
    if t%2 == 1:
        return all(a)
    return any(a)


def f21(s, t=0):
    if s <= 116:
        if t in [2,4]:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(s-7, t+1), f21(s//3, t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)


a = []
for s in range(117, 10001):
    if f19b(s):
        a.append(s)
print(a[-1])

a = []
for s in range(117, 10001):
    if f20(s):
        a.append(s)
print(a[0], a[-1])

a = []
for s in range(117, 10001):
    if f21(s) and not f19(s):
        a.append(s)
print(a[-1])


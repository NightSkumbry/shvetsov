
def f19(s, t=0):
    if s >= 301:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(s+3, t+1), f19(s*5, t+1)]
    
    if t % 2 == 0:
        return all(a)
    return any(a)


def f20(s, t=0):
    if s >= 301:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(s+3, t+1), f20(s*5, t+1)]
    
    if t % 2 == 0:
        return any(a)
    return all(a)


def f21(s, t=0):
    if s >= 301:
        if t in [2,4]:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(s+3, t+1), f21(s*5, t+1)]
    
    if t % 2 == 0:
        return all(a)
    return any(a)


for s in range(1, 301):
    if f19(s):
        print(s)
        break


a = []
for s in range(1, 301):
    if f20(s):
        a.append(s)
print(*a[:2])


for s in range(1, 301):
    if f21(s) and not f19(s):
        print(s)
        break


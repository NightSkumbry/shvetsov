
def f19(s, t=0):
    if s >= 100:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(s+2, t+1), f19(s+4, t+1)]

    if t%2 == 0:
        return any(a)
    return all(a)

for s in range(1, 100):
    if f19(s):
        print(s)
        break


def f20l(s, t=0):
    if s >= 100:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20l(s+2, t+1), f20l(s+4, t+1)]

    if t%2 == 1:
        return any(a)
    return all(a)

def f20(s, t=0):
    if s >= 100:
        if t in [3, 5]:
            return True
        return False
    if t >= 5:
        return False
    
    a = [f20(s+2, t+1), f20(s+4, t+1)]

    if t%2 == 1:
        return any(a)
    return all(a)

ans = []
for s in range(1, 100):
    if f20(s) and not f20l(s):
        ans.append(s)
print(*ans)
        
def f21l(s, t=0):
    if s >= 100:
        if t in [2]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f21l(s+2, t+1), f21l(s+4, t+1), f21l(s*2, t+1)]

    if t%2 == 0:
        return any(a)
    return all(a)

def f21(s, t=0):
    if s >= 100:
        if t in [2, 4]:
            return True
        return False
    if t >= 5:
        return False
    
    a = [f21(s+2, t+1), f21(s+4, t+1), f21(s*2, t+1)]

    if t%2 == 0:
        return any(a)
    return all(a)

a = []
for s in range(1, 100):
    if f21(s) and not f21l(s):
        a.append(s)
print(a, a[0], a[-1])

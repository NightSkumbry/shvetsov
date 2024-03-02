
def f19_b(x, y=11, t=0):
    if x+y >= 342:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19_b(x+2, y, t+1), f19_b(x*5, y, t+1), f19_b(x, y+2, t+1), f19_b(x, y*5, t+1)]

    return any(a)

def f19(x, y=11, t=0):
    if x+y >= 342:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(x+2, y, t+1), f19(x*5, y, t+1), f19(x, y+2, t+1), f19(x, y*5, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)

def f20(x, y=11, t=0):
    if x+y >= 342:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(x+2, y, t+1), f20(x*5, y, t+1), f20(x, y+2, t+1), f20(x, y*5, t+1)]

    if t%2 == 1:
        return all(a)
    return any(a)

def f21(x, y=11, t=0):
    if x+y >= 342:
        if t in [2, 4]:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(x+2, y, t+1), f21(x*5, y, t+1), f21(x, y+2, t+1), f21(x, y*5, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)

for s in range(1, 326):
    if f19_b(s):
        print(s)
        break

a = []
for s in range(1, 326):
    if f20(s):
        a.append(s)
print(a[0], a[1])

for s in range(1, 326):
    if f21(s) and not f19(s):
        print(s)
        break



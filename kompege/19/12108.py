
def f19(x, y, t=0):
    if x + y >= 275:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(x+7, y, t+1), f19(x+3, y, t+1), f19(x*4, y, t+1), f19(x, y+7, t+1), f19(x, y+3, t+1), f19(x, y*4, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)

def f20(x, y, t=0):
    if x + y >= 275:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(x+7, y, t+1), f20(x+3, y, t+1), f20(x*4, y, t+1), f20(x, y+7, t+1), f20(x, y+3, t+1), f20(x, y*4, t+1)]

    if t%2 == 1:
        return all(a)
    return any(a)

def f21(x, y, t=0):
    if x + y >= 275:
        if t in [2, 4]:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(x+7, y, t+1), f21(x+3, y, t+1), f21(x*4, y, t+1), f21(x, y+7, t+1), f21(x, y+3, t+1), f21(x, y*4, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)


for s in range(1, 217):
    if f19(s, 58):
        print(s)
        break

a = []
for s in range(1, 217):
    if f20(s, 58):
        a.append(s)
print(a[0], a[-1])

for s in range(1, 217):
    if f21(s, 58) and not f19(s, 58):
        print(s)
        break


def f19(x, y, t=0):
    if x+y >= 231:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(x+1, y, t+1), f19(x*2, t, t+1), f19(x, y+1, t+1), f19(x, y*2, t+1)]
    
    # if t%2 == 0:
    #     return all(a)
    return any(a)

def f19n(x, y, t=0):
    if x+y >= 231:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19n(x+1, y, t+1), f19n(x*2, t, t+1), f19n(x, y+1, t+1), f19n(x, y*2, t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)

def f20(x, y, t=0):
    if x+y >= 231:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(x+1, y, t+1), f20(x*2, t, t+1), f20(x, y+1, t+1), f20(x, y*2, t+1)]
    
    if t%2 == 1:
        return all(a)
    return any(a)

def f21(x, y, t=0):
    if x+y >= 231:
        if t in [2, 4]:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(x+1, y, t+1), f21(x*2, t, t+1), f21(x, y+1, t+1), f21(x, y*2, t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)

for s in range(1, 214):
    if f19(17, s):
        print(s)
        break


a = []
for s in range(1, 214):
    if f20(17, s):
        a.append(s)
print(a)


for s in range(1, 214):
    if f21(17, s) and not f19n(17, s):
        print(s)
        break



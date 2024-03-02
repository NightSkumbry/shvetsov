wc = lambda x: x <= 45
lc = lambda x: x > 45
ec = lambda x: x >= 25


def f19(s, t=0):
    if ec(s):
        if t in [2]:
            return wc(s)
        return lc(s)
    if t >= 2:
        return False
    
    a = [f19(s+1, t+1), f19(s*2, t+1)]
    
    return any(a)

def f19n(s, t=0):
    if ec(s):
        if t in [2]:
            return wc(s)
        return lc(s)
    if t >= 2:
        return False
    
    a = [f19n(s+1, t+1), f19n(s*2, t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)

def f20(s, t=0):
    if ec(s):
        if t in [3]:
            return wc(s)
        # if t in [1]:
        return False
        # return lc(s)
    if t >= 3:
        return False
    
    a = [f20(s+1, t+1), f20(s*2, t+1)]
    
    if t%2 == 1:
        return all(a)
    return any(a)

def f21(s, t=0):
    if ec(s):
        if t in [2, 4]:
            return wc(s)
        return lc(s)
    if t >= 4:
        return False
    
    a = [f21(s+1, t+1), f21(s*2, t+1)]
    
    if t%2 == 0:
        return all(a)
    return any(a)


for s in range(1, 25):
    if f19(s):
        print(s)
        break

a = []
for s in range(1, 25):
    if f20(s):
        a.append(s)
print(*a)

for s in range(1, 25):
    if f21(s) and not f19n(s):
        print(s)



# 7
# 6 11
# 10
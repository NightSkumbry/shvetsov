
def f19(x, y, t=0):
    if x + y >= 99:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f19(x*3, y, t+1), f19(x, y*3, t+1), f19(x+1, y, t+1), f19(x, y+1, t+1)]
    
    return any(a)

def f20(x, y, t=0):
    if x + y >= 99:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(x*3, y, t+1), f20(x, y*3, t+1), f20(x+1, y, t+1), f20(x, y+1, t+1)]
    
    if t % 2 == 1:
        return all(a)
    return any(a)

from functools import cache

@cache
def f21(x, y, t=0):
    if x + y >= 99:
        if t % 2 == 0:
            return True
        return False
    
    a = [f21(x*3, y, t+1), f21(x, y*3, t+1), f21(x+1, y, t+1), f21(x, y+1, t+1)]
    
    if t % 2 == 0:
        return all(a)
    return any(a)

for s in range(1, 91):
    if f19(8, s):
        print(s)
        break

a = []
for s in range(1, 91):
    if f20(8, s):
        a.append(s)
print(a, len(a))

a = []
for s in range(1, 91):
    if f21(8, s):
        a.append(s)
print(a, max(a))


# 11
# 3
# 30

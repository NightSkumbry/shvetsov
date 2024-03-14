
def f19(x,y,t=0):
    if x+y >= 83:
        if t == 2:
            return True
        return False
    if t>= 2:
        return False
    
    a = [f19(x+1,y,t+1), f19(x*4,y,t+1), f19(x,y+1,t+1), f19(x,y*4,t+1)]
    
    return any(a)


for s in range(1, 78):
    if f19(5, s):
        print(s)
        break


def f20(x,y,t=0):
    if x+y >= 83:
        if t == 3:
            return True
        return False
    if t>= 3:
        return False
    
    a = [f20(x+1,y,t+1), f20(x*4,y,t+1), f20(x,y+1,t+1), f20(x,y*4,t+1)]
    
    if t%2 == 0:
        return any(a)
    return all(a)

ans = []
for s in range(1, 78):
    if f20(5, s):
        ans.append(s)
print(ans, ans[0], ans[-1])


def f21(x,y,t=0):
    if x+y >= 83:
        if t in [2,4]:
            return True
        return False
    if t>= 4:
        return False
    
    a = [f21(x+1,y,t+1), f21(x*4,y,t+1), f21(x,y+1,t+1), f21(x,y*4,t+1)]
    
    if t%2 == 1:
        return any(a)
    return all(a)


def f21_dop(x,y,t=0):
    if x+y >= 83:
        if t == 2:
            return True
        return False
    if t>= 2:
        return False
    
    a = [f21_dop(x+1,y,t+1), f21_dop(x*4,y,t+1), f21_dop(x,y+1,t+1), f21_dop(x,y*4,t+1)]
    
    if t%2 == 1:
        return any(a)
    return all(a)


for s in range(1, 78):
    if f21(5,s) and not f21_dop(5, s):
        print(s)

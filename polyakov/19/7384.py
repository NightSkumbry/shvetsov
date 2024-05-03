

def f19(s, t=0):
    if s >= 61:
        if t == 1:
            return True
        return False
    if t >= 1:
        return False
    
    a = [f19(s+1, t+1)]
    if s <= 80-s:
        a.append(f19(s*2, t+1))
    
    if t%2 == 0:
        return any(a)
    return all(a)


ans = 0
for i in range(1, 61):
    if f19(i):
        ans += 1
print(ans)


def f20(s, t=0):
    if s >= 61:
        if t == 3:
            return True
        return False
    if t >= 3:
        return False
    
    a = [f20(s+1, t+1)]
    if s <= 80-s:
        a.append(f20(s*2, t+1))
    
    if t%2 == 0:
        return any(a)
    return all(a)


ans = []
for i in range(1, 61):
    if f20(i):
        ans.append(i)
print(ans, *ans[:2])


def f21_dop(s, t=0):
    if s >= 61:
        if t == 2:
            return True
        return False
    if t >= 2:
        return False
    
    a = [f21_dop(s+1, t+1)]
    if s <= 80-s:
        a.append(f21_dop(s*2, t+1))
    
    if t%2 == 1:
        return any(a)
    return all(a)


def f21(s, t=0):
    if s >= 61:
        if t in [2, 4]:
            return True
        return False
    if t >= 4:
        return False
    
    a = [f21(s+1, t+1)]
    if s <= 80-s:
        a.append(f21(s*2, t+1))
    
    if t%2 == 1:
        return any(a)
    return all(a)


for i in range(1, 61):
    if f21(i) and not f21_dop(i):
        print(i)




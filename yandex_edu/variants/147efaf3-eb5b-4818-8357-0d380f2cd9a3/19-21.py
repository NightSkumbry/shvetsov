
def f19(s, t=0):
    if t == 1 and s >= 200:
        return False
    if t == 2 and s >= 200:
        return True
    if t >= 2:
        return False
    
    a = [f19(s+1, t+1), f19(s*3, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)

for m in range(1, 200):
    if f19(m):
        print(m)
        break


def f20(s, t=0):
    if t == 1 and s >= 200:
        return False
    if t == 2 and s >= 200:
        return False
    if t == 3 and s >= 200:
        return True
    if t >= 3:
        return False
    
    a = [f20(s+1, t+1), f20(s*3, t+1)]

    if t%2 == 0:
        return any(a)
    return all(a)


a = 0
ans = []
for m in range(1, 200):
    if f20(m):
        a += 1
        ans.append(m)
print(*ans)


def f21(s, t=0):
    if t == 1 and s >= 200:
        return False
    if t == 2 and s >= 200:
        return True
    if t == 3 and s >= 200:
        return False
    if t == 4 and s >= 200:
        return True
    if t >= 4:
        return False
    
    a = [f21(s+1, t+1), f21(s*3, t+1)]

    if t%2 == 0:
        return all(a)
    return any(a)


for m in range(1, 200):
    if f21(m) and not f19(m):
        print(m)
        break


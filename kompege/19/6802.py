
def f19(s, t=0):
    if sum(s) >= 97:
        if t in [2]:
            return True
        return False
    if t >= 2:
        return False
    
    a = []
    for i in range(len(s)):
        a += [f19(s[:i] + [s[i] + k] + s[i+1:], t+1) for k in [1,3,5,7,8,12]]
    
    if t%2 == 0:
        return all(a)
    return any(a)


def f20(s, t=0):
    if sum(s) >= 97:
        if t in [1]:
            return True
        return False
    if t >= 1:
        return False
    
    a = []
    for i in range(len(s)):
        a += [f20(s[:i] + [s[i] + k] + s[i+1:], t+1) for k in [1,3,5,7,8,12]]
    
    return any(a)


def f21(s, t=0):
    if sum(s) >= 97:
        if t in [3]:
            return True
        return False
    if t >= 3:
        return False
    
    a = []
    for i in range(len(s)):
        a += [f21(s[:i] + [s[i] + k] + s[i+1:], t+1) for k in [1,3,5,7,8,12]]
    
    if t%2 == 0:
        return any(a)
    return all(a)


for s in range(1, 100):
    for m in range(2, 21):
        if f19([m + m*i for i in range(s)]):
            print(s)
            break
    else:
        continue
    break

a = []
for s in range(1, 100):
    for m in range(2, 21):
        if f20([m + m*i for i in range(s)]):
            a.append(s)
print(a[-1])

a = []
for s in range(1, 100):
    for m in range(2, 21):
        if f21([m + m*i for i in range(s)]):
            a.append(s)
print(a[-1], a[0])

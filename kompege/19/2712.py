

def f19(x, y, t=0):
    if max(x, y) >= 50:
        if t == 3:
            return x + y <= 109
        if t == 1:
            return False
        return x + y > 109
    if t >= 3:
        return False
    
    a = [f19(x+1, y, t+1), f19(x, y+1, t+1), # А
         f19(x+2, y, t+1), f19(x, y+2, t+1), # Б
         f19(x*2, y, t+1), f19(x, y*2, t+1)] # В
    
    if t%2 == 0:
        if any(a[:2]):
            return 'А'
        if any(a[2:4]):
            return 'Б'
        if any(a[4:]):
            return 'В'
        return False
    return all(a)


ans = ''
for s in range(1, 50):
    f = f19(24, s)
    if f:
        ans += f
        if len(ans) == 3:
            break
print(ans)







def f20_dop1(x, y, t=0):
    if max(x, y) >= 50:
        if t == 2:
            return x + y <= 109
        return x + y > 109
    if t >= 2:
        return False
    
    a = [f20_dop1(x+1, y, t+1), f20_dop1(x, y+1, t+1), # А
         f20_dop1(x+2, y, t+1), f20_dop1(x, y+2, t+1), # Б
         f20_dop1(x*2, y, t+1), f20_dop1(x, y*2, t+1)] # В
    
    if t%2 == 0:
        return all(a)
    return any(a)


def f20_dop2(x, y, t=0):
    if max(x, y) >= 50:
        if t in [2, 4]:
            return x + y <= 109
        return x + y > 109
    if t >= 4:
        return False
    
    a = [f20_dop2(x+1, y, t+1), f20_dop2(x, y+1, t+1), # А
         f20_dop2(x+2, y, t+1), f20_dop2(x, y+2, t+1), # Б
         f20_dop2(x*2, y, t+1), f20_dop2(x, y*2, t+1)] # В

    if t%2 == 0:
        return all(a)
    return any(a)


def f20(x, y, t=0):
    if max(x, y) >= 50:
        if t in [2, 4]:
            return x + y <= 109
        return x + y > 109
    if t >= 4:
        return False
    
    a = [f20(x+1, y, t+1), f20(x, y+1, t+1), # А
         f20(x+2, y, t+1), f20(x, y+2, t+1), # Б
         f20(x*2, y, t+1), f20(x, y*2, t+1)] # В

    if t%2 == 0:
        if not all(a):
            return 0
        return sum(a)
    return sum(a)


for s in range(1, 50):
    if f20_dop2(24, s) and not f20_dop1(24, s):
        print(f20(24, s))
        break


for s1 in range(1, 50):
    for s in range(1, 50):
        if f20_dop2(s1, s) and not f20_dop1(s1, s):
            print(s1)
            break
    else:
        continue
    break




# 19: 10
# 20: 4
# 21: 4 47

def f19(s, t=0):
    if t == 1 and sum(s) >= 91:
        return sum(s) > 110
    if t == 2 and sum(s) >= 91:
        return sum(s) <= 110
    if t >= 2:
        return False
    
    a = [f19( (s[0]+1, s[1]), t+1 ), f19( (s[0], s[1]+1), t+1 ), f19( (s[0]*2, s[1]), t+1 ), f19( (s[0], s[1]*2), t+1 )]
    
    if t%2 == 0:
        return all(a)
    return any(a)
    
for i in range(1, 51):
    if f19((40, i)):
        print(i)
        break

def f20(s, t=0):
    if t == 1 and sum(s) >= 91:
        return False # Не может выиграть за 1 ход
    if t == 2 and sum(s) >= 91:
        return sum(s) > 110
    if t == 3 and sum(s) >= 91:
        return sum(s) <= 110
    if t >= 3:
        return False
    
    a = [f20( (s[0]+1, s[1]), t+1 ), f20( (s[0], s[1]+1), t+1 ), f20( (s[0]*2, s[1]), t+1 ), f20( (s[0], s[1]*2), t+1 )]
    
    if t % 2 == 0:
        return any(a)
    return all(a)
        
ans = 0
for i in range(1, 51):
    if f20((40, i)):
        ans += 1

print(ans)


def f21(s, t=0):
    if t == 1 and sum(s) >= 91:
        return sum(s) > 110
    if t == 2 and sum(s) >= 91:
        return sum(s) <= 110
    if t == 3 and sum(s) >= 91:
        return sum(s) > 110
    if t == 4 and sum(s) >= 91:
        return sum(s) <= 110
    if t >= 4:
        return False
    
    a = [f21( (s[0]+1, s[1]), t+1 ), f21( (s[0], s[1]+1), t+1 ), f21( (s[0]*2, s[1]), t+1 ), f21( (s[0], s[1]*2), t+1 )]
    
    if t % 2 == 0:
        return all(a)
    return any(a)


m = 51
m1 = 0
for i in range(1, 51):
    if f21((40, i)) and not f19((40, i)):
        m = min(m, i)
        m1 = max(m1, i)

print(m, m1)




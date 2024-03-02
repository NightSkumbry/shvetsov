

def f(player, w, c=''):
    if c in w or len(w) == 1:
        if len(w) == 1:
            c = w[0]
        if len(c)%2 == 1-player:
            return {c}
        return set()
    
    w = list(filter(lambda x: c == x[:len(c)], w))
    l = set(map(lambda x: x[len(c)], w))

    if len(c)%2 == player:
        a = set()
        for i in l:
            a |= f(player, w, c+i)
        return a
    a = set()
    for i in l:
        g = f(player, w, c+i)
        if g:
            a |= g
        else:
            a = set()
            break
    return a



print(len(f(0, 'ПАТРОНИМ ПАУЗОК ПАЯЦ ПАТРОНИРОВАТЬ ПАТРОНЕССА ПАШНЯ ПАТРОНТАШ ПАТРОННИК ПАЯСНИЧАТЬ'.split())))
print(max(map(len, f(1, 'ЗЕМЛЯНИКА ЗЕМЛЯНКА ЗЛАК ЗЛАТО ЗИМНИК ЗИМОВЬЕ'.split()))))
from itertools import product as pr
a = 0
for h in pr('AB', repeat=3):
    h = ''.join(h)
    for s in pr('AB', repeat=6):
        s = ''.join(s)
        if f(1, [h, s]):
            a += 1
print(a)



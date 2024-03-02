

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

g = len(f(0, 'АБВГДАБВГДХ ДГВБАДГВБЕ'.split()))
print('П' + str(len(f(0, 'АБВГДАБВГДХ ДГВБАДГВБЕ'.split()))) if g else 'В' + str(len(f(1, 'АБВГДАБВГДХ ДГВБАДГВБЕ'.split()))))

from itertools import permutations
for i in permutations('ДГВБАДГВБЕ'):
    i = ''.join(i)
    if sum([k!=l for k,l in zip(i, 'ДГВБАДГВБЕ')]) == 2 and f(1, ['АБВГДАБВГДХ', i]):
        print(i)
        break

g = len(f(0, 'ВОРОНА ВОЛК ВОЛНА МОРИС МОРЯНА МОРКОВЬ'.split()))
print('П' + str(len(f(0, 'ВОРОНА ВОЛК ВОЛНА МОРИС МОРЯНА МОРКОВЬ'.split()))) if g else 'В' + str(len(f(1, 'ВОРОНА ВОЛК ВОЛНА МОРИС МОРЯНА МОРКОВЬ'.split()))))



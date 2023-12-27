
def f(a, b):
    return [a+1, b], [a*2, b], [a, b+1], [a, b*2]





for s in range(1, 51):
    p = f(40, s)
    if all([any([j[0] + j[1] in range(91, 111) for j in f(*i)]) for i in p]) and not any([i[0] + i[1] in range(91, 111) for i in p]):
        # print(s)
        ...

ans = 0
for s in range(1, 51):
    p = f(40, s)
    if not any([i[0] + i[1] in range(91, 111) for i in p]):
        d = False
        for k in p:
            p1 = f(k[0], k[1])
            if all([any([j[0] + j[1] in range(91, 111) for j in f(*i)]) for i in p1]) and not any([i[0] + i[1] in range(91, 111) for i in p1]):
                d = True
        ans += d
# print(ans)



for s in range(1, 51):
    p = f(40, s)
    if not any([i[0] + i[1] >= 91 for i in p]):
        g = False
        d = 4
        for k in p:
            p1 = f(k[0], k[1])
            if all([any([j[0] + j[1] in range(91, 111) for j in f(*i)]) for i in p1]):
                d -= 1
            else:
                g = 4
                for l in p1:
                    p2 = f(l[0], l[1])
                    if all([any([j[0] + j[1] in range(91, 111) for j in f(*i)]) for i in p2]) and not any([i[0] + i[1] in range(91, 111) for i in p2]):
                        g = True
                    
                
        if d and g:
            print(s)
            


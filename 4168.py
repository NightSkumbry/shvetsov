a = abs(7**500+7**200-7**50)
m = 0
for x in range(1, a):
    b = a-x
    p = []
    while b > 0:
        p.append(b%7)
        b//=7
    m = max(m, sum(p))
print(m)
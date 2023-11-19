a = abs(7**500+7**200-7**50)
m = 0

p = []
while a > 0:
    p.append(a%7)
    a//=7

print(6*(len(p)-1))
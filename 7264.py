a = 343**515 - 6* 49**520 + 5* 49**510 - 3* 7**530 - 550

r = []
while a > 0:
    r.append(a%7)
    a//=7
print(r.count(6))

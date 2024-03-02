from math import gcd
od = lambda x, y: gcd(x, y) > 1
def test(a):
    for x in range(1, 10000):
        k = (od(x, 42) <= (not od(x, 7))) or (x + a >= 25)
        if not k:
            return False
    return True
        
for a in range(1, 10000):
    if test(a):
        print(a)
        break
    




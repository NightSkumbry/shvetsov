
def test(A):
    for x in range(100000):
        k = ((x & 156 != 0) or (x & 436 != 0) <= (x & A > 0))
        if not k:
            return False
    return True
        

for a in range(1, 10000):
    if test(a):
        print(a) # -> 288
        break






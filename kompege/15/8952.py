def test(a):
    for x in range(1, 100000):
        k = ((x & 103 == 0) and (x & 94 != 0)) <= (x & a != 0)
        if not k:
            return False
    return True


for a in range(100000):
    if test(a):
        print(a)
        break
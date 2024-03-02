def test(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            k = (x + 2*y != 58) or ((a - x > 0) == (a + y > 0))
            if not k:
                return False
    return True

for a in range(10000):
    if test(a):
        print(a)
        break
    
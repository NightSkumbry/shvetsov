def test(a):
    for x in range(1000):
        for y in range(1000):
            k = (x >= 11) or (3 * x < y) or (x*y < a)
            if not k:
                return False
    return True

for a in range(10000):
    if test(a):
        print(a)
        break
    
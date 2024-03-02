def test(a):
    for x in range(1000):
        for y in range(1000):
            k = (3*x + 2*y > 25) or (x > 2*y) or (x + 4*y < a)
            if not k:
                return True
    return False


for a in range(10000):
    if test(a):
        print(a)
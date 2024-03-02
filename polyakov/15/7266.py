def test(a):
    for x in range(1000):
        for y in range(1000):
            k = (3*x + 2*y > 95) or (4*x < 3*y) or (x + 4*y < a)
            if not k:
                return True
    return False


for a in range(10000):
    if test(a):
        print(a)
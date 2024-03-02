def test(a):
    for x in range(1000):
        for y in range(1000):
            k = (x*y < a) or (x < y) or (9 < x)
            if not k:
                return False
    return True


for a in range(19000):
    if test(a):
        print(a)
        break
    
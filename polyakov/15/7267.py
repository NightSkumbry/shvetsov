
def test(a):
    for x in range(1000):
        for y in range(1000):
            k = (4*x + y > 115) or (x > 3*y) or (x + 4*y < a)
            if not k:
                return True
    return False


for a in range(10000):
    if test(a):
        print(a)









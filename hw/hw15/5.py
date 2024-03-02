
def test(a):
    for x in range(1, 100000):
        k = (a+x < 123) <= ((x%5 == 0) <= (not (x%7 == 0)))
        if not k:
            return False
    return  True

for a in range(10000):
    if test(a):
        print(a)
        break


# 88 


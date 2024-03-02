def test(a):
    for x in range(1000):
        for y in range(1000):
            k = (x + 3*y != 27) or ((a > x) and (a > y))
            if not k:
                return False
    return True


for a in range(-10000, 10000):
    # print(a)
    if test(a):
        print(a)
        break
    
    
    
# 28
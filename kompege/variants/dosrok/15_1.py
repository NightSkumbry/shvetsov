
def test(A):
    for x in range(1, 100000):
        k = (not (x%A == 0)) <= ((x%28 == 0) <= (not (x%49 == 0)))
        if not k:
            return False
    return True


for a in range(1, 100000):
    if test(a):
        print(a)






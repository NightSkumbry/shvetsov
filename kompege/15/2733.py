
def test(A):
    for x in range(1000):
        for y in range(1000):
            k = (x > 56) or (y >= x) or (3*x - y < A)
            if not k:
                return False
    return True


for a in range(1000):
    if test(a):
        print(a)
        break




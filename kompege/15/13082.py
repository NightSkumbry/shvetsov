
def test(A):
    for x in range(1000):
        for y in range(1000):
            k = (3*x + y > 48) or (x > y) or (4*x + y < A)
            if not k:
                return True
    return False

for a in range(100000):
    if test(a):
        print(a)




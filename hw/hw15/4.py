def test(a):
    for x in range(100000):
        k = ((x & 8375 != 0) or (x & 6743 != 0)) <= (x & a > 0)
        if not k:
            return False
    return True


for a in range(100000):
    if test(a):
        print(a)
        break

# небольшой анализ:
print(8375|6743)
# 15095


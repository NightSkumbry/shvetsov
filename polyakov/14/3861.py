for x in range(1, 10000):
    a = 27**7 - 3**11 + 36 - x
    r = 0
    while a:
        r += a%3
        a //= 3
    if r == 22:
        print(x)
        break




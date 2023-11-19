for x in range(10):
    a = [3,0,1]
    b = [2,0,1]
    r = 0
    for i, e in enumerate(a):
        r += e * int(f'123{x}4')**i
    for i, e in enumerate(b):
        r += e * int(f'12{x}43')**i
    if r % 50 == 0:
        print(r//50)
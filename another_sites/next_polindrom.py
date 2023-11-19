def f():
    n = input().strip()
    ni = int(n) + 1
    n = str(ni)
    if len(n) % 2 == 1:
        a = n[:int(len(n)/2)][::-1]
        m = n[int(len(n)/2)]
        b = n[int(len(n)/2)+1:]
        if int(a) - int(b) >= 0:
            print(a[::-1]+m+a)
            return
        if int(m) < 9:
            print(a[::-1]+str(int(m)+1)+a)
            return
        a = str(int(a[::-1]) + 1)
        print(a+'0'+a[::-1])
        return
    a = n[:int(len(n)/2)][::-1]
    b = n[int(len(n)/2):]
    if int(a) - int(b) >= 0:
        print(a[::-1]+a)
        return
    a = str(int(a[::-1]) + 1)
    print(a+a[::-1])
    return


f()
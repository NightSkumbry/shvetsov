
for x in range(13):
    a = [1,2,1,x,8]
    b = [5,7,5,x,7]
    ar = 0
    br = 0
    for i, e in enumerate(a):
        ar += e*13**i
    for i, e in enumerate(b):
        br += e*13**i
    
    if (ar-br) % 19 == 0:
        print((ar-br)//19)
        break









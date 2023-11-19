for i in range(1000):
    n = bin(i)[2:].zfill(3)
    n += n[-3:] * (i%5==0)
    n += bin(i%5*5)[2:] * (i%5!=0)
    if int(n, 2) > 256:
        print(i)
        break
    
    
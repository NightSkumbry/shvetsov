for i in range(1, 100000):
    n = list(map(int, str(i)))
    r = abs(sum(n[1::2])-sum(map(lambda x: x*(x%2==0), n)))
    if r == 13:
        print(i)
        break
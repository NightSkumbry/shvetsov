
def F(file):
    with open(f'./hw/hw17/27-41{file}.txt') as f:
        N = int(f.readline())
        a = [list(map(int, i.split())) for i in f]

    ASS = 1 - (sum(map(sum, a)) % 2)
    
    b = [10**1000, 10**1000]
    b[a[0][0]%2] = a[0][0]
    b[a[0][1]%2] = min(b[a[0][1]%2], a[0][1])
    b[a[0][2]%2] = min(b[a[0][2]%2], a[0][2])
    
    for i in a[1:]:
        p1 = [i[0] + b[0],   i[1] + b[0],   i[2] + b[0]]
        p2 = [i[0] + b[1],   i[1] + b[1],   i[2] + b[1]]
        p = []
        if b[0] != 10**1000: p += p1
        if b[1] != 10**1000: p += p2
        b[0] = min(list(filter(lambda x: x%2 == 0, p)) + [10**1000])
        b[1] = min(list(filter(lambda x: x%2 == 1, p)) + [10**1000])
    
    print(b[ASS])



F('t')
F('a')
F('b')






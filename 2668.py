def A(): # 11009
    with open('./files/27-8a.txt') as f:
        a = list(map(lambda x: int(x)**2, f.read().strip().split('\n')[1:]))
    m = 10**10
    for i in range(0, len(a)-5):
        for j in range(i+5, len(a)):
            m = min(m, a[i]+a[j])
    print(m)
    

A()


def B():
    with open('./files/27-8b.txt') as f:
        a = list(map(lambda x: int(x)**2, f.read().strip().split('\n')[1:]))
    b = []
    while a[len(b)+5:]:
        m = min(a[len(b)+5:])
        mi = len(a)-a[::-1].index(m)-1
        for i in a[len(b):mi-4]:
            b.append(m+i)
    print(min(b))
            
B()


    
    
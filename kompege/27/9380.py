import math

def F1(a, n, p):
    ans = 0
    for i in range(1, n+1):
        ans += i*a[(p+i)%len(a)]
        ans += i*a[(p-i)%len(a)]
    if len(a) % 2 == 0:
        ans -= n*a[(p+n)%len(a)]
    return ans


def F2(a, n, p):
    ans = 0
    for i in range(1, n):
        ans += i*a[(p+i)%len(a)]
    return ans


def A():
    with open('./files/27A_9380.txt') as f:
        a = f.read().strip().split('\n')
        k = int(a[0].split()[1])
        a = list(map(lambda x: math.ceil(int(x)/k), a[1:]))
    ans = 0
    for i in range(len(a)):
        i1 = 0
        i2 = 0
        k1 = 0
        k2 = 0
        for j in range(len(a)-1):
            if k1 > k2:
                i2 += 1
                k2 += i2*a[(i-i2)%len(a)]
            else:
                i1 += 1
                k1 += i1*a[(i+i1)%len(a)]
        if k1 == k2:
            ans = i
    print(ans)




def B():
    with open('./files/27B_9380.txt') as f:
        a = f.read().strip().split('\n')
        k = int(a[0].split()[1])
        a = list(map(lambda x: math.ceil(int(x)/k), a[1:]))
    n = len(a)//2
    
    a3 = [a[i]*2-a[(i-n)%len(a)]-a[(i+n)%len(a)] for i in range(len(a))]
    a1 = [F1(a, n, 0), F1(a, n, 1)]
    a2 = [a1[1]-a1[0]]
    for i in a3[1:]:
        a2.append(a2[-1]+i)
    for i in a2[1:-1]:
        a1.append(a1[-1]+i)

    
    


import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))


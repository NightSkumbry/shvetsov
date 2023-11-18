
def A():
    with open('./files/27A_2728.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    m = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i]+a[j]) % 2 == 0 and (a[j]%23 == 0 or a[i]%23 == 0):
                m = max(m, a[j]+a[i])
    print(m)


def B():
    with open('./files/27B_2728.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    m = max(map(lambda x: x*(x%23==0 and x%2==0), a))
    a1 = a.copy()
    a1.pop(a.index(m))
    maxi = m+max(map(lambda x: x*(x%2==0), a1))
    m = max(map(lambda x: x*(x%23==0 and x%2==1), a))
    a1 = a.copy()
    a1.pop(a.index(m))
    maxi = max(maxi, m+max(map(lambda x: x*(x%2==1), a1)))
    print(maxi)




A()
import timeit
print(timeit.timeit(B, number=1))

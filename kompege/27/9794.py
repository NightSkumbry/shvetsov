def A(): # 43666
    with open('./files/27_A_9794.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]
    a.sort()
    ans = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] >= k:
                ans += 1
    print(ans)

import math
def B():
    with open('./files/27_B_9794.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]
        a = a[2:]
        a.sort()
    a = a[::-1]
    al = 0
    ans = 0
    b = []
    
    for i in a:
        if i >= k:
            ans += al
            al += 1
        elif i >= math.ceil(k/2):
            ans += al + len(b)
            b.append(i)
        else:
            ans += al
            while b and b[-1] < k-i:
                b.pop()
            ans += len(b)
    print(ans)
            
    




A()
import timeit
print(timeit.timeit(B, number=1))

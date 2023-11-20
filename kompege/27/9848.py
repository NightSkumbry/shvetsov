
def A():
    with open('./files/27_A_9848.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]+1
        a = a[2:]
    b = [a[0]]
    for i in a[1:]:
        b.append(b[-1]+i)
    ans = 0
    m = 0
    for i in range(k, len(b)):
        m = min(m, b[i-k])
        ans = max(ans, b[i]-m)
    print(ans)





def B():
    with open('./files/27_B_9848.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
        k = a[0]+1
        a = a[2:]
    b = [a[0]]
    for i in a[1:]:
        b.append(b[-1]+i)
    ans = 0
    m = 0
    for i in range(k, len(b)):
        m = min(m, b[i-k])
        ans = max(ans, b[i]-m)
    print(ans)    
    
            
            
    




A()
import timeit
print(timeit.timeit(B, number=1))


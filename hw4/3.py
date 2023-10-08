import random

a = random.randint(1, 10000000)

def f(n):
    n = list(map(int, '00' + str(n)))[::-1]
    nuls = 0
    while n[0] == 0:
        nuls += 1
        n.pop(0)

    if n[1] < 9:
        n[0] -= 1
        n[1] += 1
        i = 1
    
    elif n[1] == 9:
        i = 2
        while n[i] == 9:
            i+=1
        n[i-1] = n[0]-1
        n[0] = 9
        n[i] += 1
    
    s = ''.join(map(str, n))
    s = s[:i] + '0'*nuls + s[i:]
    return(int(s[::-1]))
        
print(f(a))


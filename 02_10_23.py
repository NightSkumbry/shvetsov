def f1():
    for i in range(154026, 154044):
        d = set()
        for k in range(1, int(i**0.5)+1):
            if i%k == 0:
                d.add(k)
                d.add(i//k)
        if len(d) == 4:
            print(*sorted(list(d))[-2:])


def f2():
    for i in range(190201, 190261):
        d = set()
        for k in range(1, int(i**0.5)+1):
            if i%k == 0:
                if k % 2 == 0:
                    d.add(k)
                if (i//k) % 2 == 0:
                    d.add(i//k)
        if len(d) == 4:
            print(*sorted(list(d))[-2:][::-1])
    

def f3():
    a = 0
    for i in range(1395, 22718):
        if str(i) == ''.join((sorted(str(i)))):
            a += i
    print(a)
    
    
def is_prime(n):
    for k in range(2, int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
    
    
import math
def f4():
    a = 0
    for i in range(math.ceil(3661**0.5), int(33625**0.5)+1):
        a += 1 * is_prime(i)
    print(a)
        


f4()
    
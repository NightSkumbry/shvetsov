# from fnmatch import fnmatchcase
from tqdm import tqdm
from functools import cache
import sys
sys.setrecursionlimit(2000)

# def sd(n):
#     res = 1
#     for i in range (2,1000) :
#         p = i
#         while(n % i == 0) :
#             n = n // i
#             p *= i
#         res *= (p - 1) // (i - 1)
#     return res

@cache
def sd(n, s=2, p=2):
    if n == 1:
        return (p-1) // (s-1)
    if n%s == 0:
        return sd(n//s, s, p*s)
    res = (p-1) // (s-1)
    while n%s:
        s+=1
    return res * sd(n, s, s)
    




def dels(n):
    d = set()
    for i in range(1, 1+int(n**0.5)):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

@cache
def is_prime(n):
    for i in range(1, 1+int(n**0.5)):
        if n%i == 0:
            return False
    return True

# for i in range(1, 30000):
#     d1 = sum(dels(i))
#     d2 = sd(i)
#     if d1 != d2:
#         print(d1, d2, d1==d2, i)
for i in tqdm(range(10**6)):
    for t in range(10):
        k = '1' + str(i) + f'3{t}9'
        # print(k)
        if is_prime(sd(int(k))):
            d = dels(int(k))
            print(k, d[-2])



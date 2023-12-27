
def A():
    with open('./files/27a_7046.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    
    n = sum(a)
    ans = 0
    r = sum(a)
    b = [0] + list(accumulate(a))
    
    for i in range(len(b)):
        for j in range(i, len(b)):
            s = abs(n-2*(b[j]-b[i]))
            if r >= s and s%73 == 0:
                if r == s:
                    ans = min(ans, j-i)
                else:
                    r = s
                    ans = j-i
    print(ans)


from itertools import accumulate
def B():
    with open('./files/27a_7046.txt') as f:
        a = list(map(int, f.read().strip().split('\n')))
    
    n = sum(a)%73 # ost
    if n % 2 == 0:
        sobol = n//2
    else:
        sobol = (73+n)//2
    ans = 0 # ans
    r = sum(a) # разница
    b = [0] + list(accumulate(a)) # ПС
    l = 0 # lind
    
    for i in range(len(b)):
        if ...:...
    
        






import timeit
print(timeit.timeit(A, number=1))

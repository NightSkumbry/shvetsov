primes = [True for i in range(int(1_850_000_000**0.5)*10)]
primes[0] = False
primes[1] = False
for i in range(int((int(1_850_000_000**0.5)*10)**0.5)+1):
    if primes[i]:
        for k in range(i**2, int(1_850_000_000**0.5)*10, i):
            primes[k] = False

pr = list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(primes))))
# print(len(pr))

def dels(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            j = n//i
            if i%2 == 0:
                d.add(i)
            if j%2 == 0:
                d.add(j)
    return len(d)


def usl(n):
    a = 0
    while n%2 == 0:
        a += 1
        n//=2
    if a % 2 == 0:
        return False
    for i in pr[1:]:
        if n%i == 0:
            a = 0
            while n%i == 0:
                a += 1
                n//=i
            if a % 2:
                return False
    return True * (n==1)
        


k = 1_850_000_000
count = 0
while True:
    k += 2
    if usl(k):
        count += 1
        print(k - 1_850_000_000, dels(k))
    if count == 5:
        break
    
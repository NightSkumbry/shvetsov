from functools import lru_cache


def dels(n):
    m = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            m.add(i)
            m.add(n//i)
    return sorted(list(m))


@lru_cache(None)
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def sdels(n):
    a = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            if is_prime(i):
                a += 1
                if a == 6:
                    return True
            else:
                return False
    return False

a = 0
for i in range(2023, 10**9, 2023):
    if sdels(i):
        a+=1
        print(i, dels(i)[-2])
        if a == 5:
            break
    
a = 0
b = []
for i in range(10**9-10**9%2023, 2023, -2023):
    if sdels(i):
        a+=1
        b.append([i, dels(i)[-2]])
        if a == 5:
            break
[print(*i) for i in b[::-1]]







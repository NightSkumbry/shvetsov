from fnmatch import fnmatchcase

def dels(n):
    d = set()
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

for i in range(10**7+1):
    if fnmatchcase(str(i), '3*52?'):
        if int(i**0.5) == i**0.5:
            print(i, dels(i)[-1])












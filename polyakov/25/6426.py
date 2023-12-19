import fnmatch


def dels(n):
    a = set()
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            a.add(i)
            a.add(n//i)
    return len(a)


for i in range(0, 10**8+1, 311):
    if fnmatch.fnmatchcase(str(i), '12?5*5??') and dels(i) == 2:
        print(i, i//311)




from fnmatch import fnmatchcase

for i in range(0, 10**8, 1923):
    if fnmatchcase(str(i), '1*2??76'):
        print(i, i//1923)







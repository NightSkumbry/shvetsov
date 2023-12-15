import fnmatch

for i in range(0, 10**8, 1923):
    if fnmatch.fnmatchcase(str(i), '1*2??76'):
        print(i, i//1923)







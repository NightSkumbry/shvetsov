from fnmatch import fnmatchcase

for i in range(0, 10**10+1, 2024):
    if fnmatchcase(str(i), '1*2322?2'):
        print(i, i//2024)








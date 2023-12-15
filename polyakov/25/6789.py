import fnmatch

for i in range(0, 10**8, 2025):
    if fnmatch.fnmatchcase(str(i), '12*34?5'):
        print(i, i//2025)





import fnmatch
for i in range(0, 10**10, 50068):
    if fnmatch.fnmatchcase(str(i), '9?979*8') and str(i).find('0') != -1:
        print(i, i//50068)




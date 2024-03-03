
from fnmatch import fnmatchcase

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


for i in range(0, 10**8+1, 311):
    if is_prime(i//311):
        if fnmatchcase(str(i), '12?5*5??'):
            print(i, i//311)



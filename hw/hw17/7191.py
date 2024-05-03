from fnmatch import fnmatchcase


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


for i in range(0, 10**9, 2267):
    if is_prime(sum(map(int, str(i)))):
        if fnmatchcase(str(i), '7*15?3*7'):
            print(i, i//2267)



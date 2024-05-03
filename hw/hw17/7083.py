import re


r = re.compile(r'1[02468]2157[13579]*4')

for i in range(133000, 10**10, 133):
    if re.fullmatch(r, str(i)):
        print(i, i//133)







from itertools import product
ans = set()

for i in product('01234567',repeat=5):
    if i[0] != '0':
        if i.count('6') == 1:
            match i.index('6'):
                case 0:
                    f = i[1] in '0246'
                case 4:
                    f = i[3] in '0246'
                case _:
                    f = i[i.index('6') - 1] in '0246' and i[i.index('6') + 1] in '0246'
            if f:
                ans.add(i)

print(len(ans))





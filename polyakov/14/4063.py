
a = 7**103 + 6*7**104 - 3*7**57 + 98
r = 0

while a:
    if a%7 == 6:
        r += 1
    a //= 7
print(r)








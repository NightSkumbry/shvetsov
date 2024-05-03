
for n in range(10000):
    b = bin(n)[2:]
    if n%2 == 0:
        b += '01'
    else:
        b = '1' + b + '1'
    if int(b, 2) > 156:
        print(n)
        break









for n in range(2, 10000):
    b = bin(n)[2:]
    b += str(int(sum(map(int, b[-2:])) == 1))
    b += str(int(sum(map(int, b[-2:])) == 1))
    if int(b, 2) > 93:
        print(n)
        break







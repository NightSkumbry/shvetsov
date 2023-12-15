
ans = 11111
for n in range(1000):
    b = bin(n)[2:]
    b += str(b.count('1')%2)
    b += str(b.count('1')%2)
    if int(b, 2) > 118:
        ans = min(ans, int(b, 2))


print(ans)





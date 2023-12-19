ans = 10000

for n in range(1, 10000):
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(int(n % 2 == 0))
    if int(b, 2) > 204:
        ans = min(ans, int(b, 2))

print(ans)



ans = 0
for i in range(1, 10000):
    b = bin(i)[2:]
    if b.count('0') == 0:
        continue
    b = b[::-1]
    b = b.replace('0', b[-2:], 1)
    if int(b, 2) == 127:
        ans += 1

print(ans)








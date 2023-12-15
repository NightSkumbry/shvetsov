
ans = 0
for i in range(10000):
    b = bin(i)[2:]
    if i % 2 == 0:
        b = f'1{b}11'
    else:
        b = f'11{b}0'
    if int(b, 2) in range(500, 1001):
        ans += 1
print(ans)








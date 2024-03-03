
ans = 0
for n in range(1_000, 10_000):
    i = oct(n)[2:].replace('0', '1').replace('2', '1').replace('4', '1').replace('6', '1')
    i += str(n%8)
    i = i.replace('0', '1').replace('2', '1').replace('4', '1').replace('6', '1')
    i += str(n%8)
    r = int(i, 8)
    if r%234 == 0:
        ans = max(ans, r)
print(ans)





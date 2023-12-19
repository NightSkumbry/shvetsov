
ans = 0
for n in range(10000, 100000):
    b = oct(n)[2:].replace('1', '2').replace('3', '2').replace('5', '2').replace('7', '2')
    b += str(n%8)
    b = b.replace('1', '2').replace('3', '2').replace('5', '2').replace('7', '2')
    b += str(n%8)
    if int(b, 8) % 2023 == 0:
        ans += n
    
print(ans)








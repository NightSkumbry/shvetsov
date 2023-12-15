
ans = 0

for x in '0123456789abcdef':
    for y in '0123456789abcdef':
        if (int(f'27A{x}23', 16) + int(f'8{y}E5D2', 16)) % 5 == 0:
            ans = max(ans, int(x, 16)+int(y, 16))



print(ans)




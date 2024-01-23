
ans = 0
for x in range(-10, 100):
    for y in range(-10, 100):
        if 0 < x < 9 and 0 < y < 9 and ((x < 3) or (x < 6 and y < 6) or (y < 3)):
            ans += 1

print(ans)





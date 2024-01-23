ans = 0

for x in range(-10, 30):
    for y in range(-10, 30):
        if (-3 <= x <= 5 and 8 <= y <= 24) or (0 <= x <= 20 and 0 <= y <= 13):
            ans += 1

print(ans)
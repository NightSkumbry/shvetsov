
ans = 0
for x in range(-50, 50):
    for y in range(-50, 50):
        if (x >= 0 and y <= 10 - x/3**0.5 and y >= x/3**0.5) or (x <= 0 and y <= 20 + x/3**0.5 and y >= 10 - x*3**0.5):
            ans += 1

print(ans)



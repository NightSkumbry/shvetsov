ans = 0
for x in range(-3, 30):
    for y in range(-3, 30):
        if x > 0 and y < -x/(3**0.5) + 10 and y > x/(3**0.5):
            ans += 1

print(ans)

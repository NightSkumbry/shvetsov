ans = 0

for x in range(-30, 30):
    for y in range(-30, 30):
        if y < -x and y > -x - 10*2**0.5 and y > x - 10*2**0.5 and y < x + 10*2**0.5:
            ans += 1

print(ans)

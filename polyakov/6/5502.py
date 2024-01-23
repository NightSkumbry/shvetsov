
ans = 0
for x in range(-2, 20):
    for y in range(-2, 20):
        if x > 0 and y < 15 - (x/3**0.5) and y > x/3**0.5:
            ans += 1

print(ans)








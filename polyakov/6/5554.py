
ans = 0
for x in range(-20, 200):
    for y in range(-200, 200):
        if y < x*3**0.5 and y < 7*3**0.5 - x*3**0.5 and y > -x*3**0.5 and y > -7*3**0.5 + x*3**0.5:
            ans += 1

print(ans)









ans = 0
for x in range(20):
    for y in range(20):
        if 2 < y < 6 and 3 < x < 12 and not (0 <= y <= 5 and 0 <= x <= 8):
            ans += 1
print(ans)






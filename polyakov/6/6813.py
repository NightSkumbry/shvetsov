
ans = 0
for x in range(-10, 10):
    for y in range(-10, 10):
        if -5 < x < 0 and -5 < y < 5 or 0 <= x < 5 and -5 < y < 0:
            ans += 1
            
print(ans)







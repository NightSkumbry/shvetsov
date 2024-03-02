from turtle import *

left(90)


for _ in range(10):
    left(60)
    fd(300)
    left(60)

ans = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x >= -(300 * (3**0.5) / 2):
            if y >= x/(3**0.5):
                if y <= -x/(3**0.5):
                    ans += 1

print(ans)

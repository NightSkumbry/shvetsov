a = (2**345 + 8**65 - 4**130) * (8**123 + 4**45 - 2**89)

r = ''
while a > 1:
    r += str(a%8)
    a //= 8

r += str(a%8) * (a != 0)
r = r[::-1]
print(sum(map(int, r)))
from functools import lru_cache

@lru_cache(2000)
def to_conv(n, s):
    h = n%s
    n //= s
    if n:
        return to_conv(n, s) + str(h)
    return str(h)

print(184827640, to_conv(184827640, 3), to_conv(184827640, 7))
print(2023**3, to_conv(184827640, 3)[::-1], to_conv(184827640, 7)[::-1])

for i in range(20, 2023**3, 10):
    if i%3==0 or i%7==0 or '2' not in str(i):
        continue
    s = to_conv(i, 7)
    if s == s[::-1] and to_conv(i, 3) == to_conv(i, 3)[::-1]:
        print(i, sum(map(int, to_conv(i, 8))))









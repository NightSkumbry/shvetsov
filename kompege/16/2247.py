
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 3:
        return n+1
    if n % 2 == 0:
        return f(n-2) + n-2
    return f(n+2) + n+2

# Если n не чётно, то опять, улетает в бесконечность
# иначе сейчас напишу цикл 
ans = 0
for i in range(0, 10000, 2):
    if len(str(f(i))) == 5:
        ans += 1
print(ans, f(i)) # f(i) для того, то бы убедиться, что оно более 5 знаков








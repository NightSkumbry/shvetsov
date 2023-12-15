import fnmatch
import math

c = 0
ans = []
for i in range(10**9 - 10**9 % math.lcm(6, 19, 2023), 10**8-1, -math.lcm(6, 19, 2023)):
    if fnmatch.fnmatchcase(str(i), '1*1*1?'):
        ans.append([i, i//2023])
        c += 1
        if c == 5:
            break

[print(*i) for i in ans[::-1]]





from fnmatch import fnmatchcase
ans = []
for i in range(0, int('22122212221', 3)+1000, 148):
    a = i
    r = ''
    while a:
        r += str(a%3)
        a //= 3
    r = r[::-1]
    if fnmatchcase(r, '2?1?2?1?2?1'):
        ans.append([i, i//148])

[print(*i) for i in ans[::-1]]

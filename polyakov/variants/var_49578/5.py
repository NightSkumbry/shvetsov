ans = 0
for i in range(1000, 10000):
    s = str(i)
    a = [int(s[0]) * int(s[1]), int(s[2]) * int(s[3])]
    a.sort()
    b = str(a[0]) + str(a[1])
    if int(b) == 1214:
        ans = max(ans, i)
        
print(ans)
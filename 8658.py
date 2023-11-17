ans = set()
for i in range(1, 10000):
    n = oct(i)[2:].zfill(2)
    if i % 7 == 0:
        n += n[-2:]
    else:
        n += oct(i%7*7)[2:]
    if int(n, 8) < 3000:
        ans.add(int(n, 8))
print(len(ans))

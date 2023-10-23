with open('./files/24-3.txt') as f:
    a = f.read().strip()

ans = 1
pr = 1
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        pr += 1
    else:
        ans = max(ans, pr)
        pr = 1
print(ans)
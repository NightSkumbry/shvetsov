
with open('./hw/hw17/24-2.txt') as f:
    a = f.read().strip()

ans = a[0]
k = a[0]
for i in a[1:]:
    if i > k[-1]:
        k += i
    else:
        if len(k) > len(ans):
            ans = k
        k = i
        
print(ans)



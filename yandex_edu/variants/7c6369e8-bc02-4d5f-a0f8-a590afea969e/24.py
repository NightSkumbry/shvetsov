# 7c6369e8-bc02-4d5f-a0f8-a590afea969e

with open('./yandex_edu/variants/7c6369e8-bc02-4d5f-a0f8-a590afea969e/24.txt') as f:
    a = f.read().strip().lower()

l = r = ans = 0
s = 'ahaha'

for i, e in enumerate(a):
    ans = max(ans, i-l+1)
    
    if a[i:i+5] == s:
        ans = max(ans, i+4-l)
        l = i+1
    
print(ans)




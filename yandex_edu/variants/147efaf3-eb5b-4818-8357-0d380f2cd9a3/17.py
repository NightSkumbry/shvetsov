
with open('./yandex_edu/variants/147efaf3-eb5b-4818-8357-0d380f2cd9a3/17.txt') as f:
    a = [int(i) for i in f]

m = max(filter(lambda x: len(str(x))==3, a))

ans= 0
ansm = 0
for i in range(len(a)-1):
    if (len(str(a[i])) == 3) ^ (len(str(a[i+1])) == 3):
        if a[i]+a[i+1] >= m:
            ans += 1
            ansm = max(ansm, a[i]+a[i+1])
        
print(ans, ansm)


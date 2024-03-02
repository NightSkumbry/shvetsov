with open('./yandex_edu/variants/147efaf3-eb5b-4818-8357-0d380f2cd9a3/9.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

ans = 0
for i in a:
    if len(set(i)) == 3:
        if sum(i)%3==0:
            ans += 1
print(ans)
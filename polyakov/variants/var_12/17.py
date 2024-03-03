with open('./polyakov/variants/var_12/17-374.txt') as f:
    a = [int(i) for i in f]

m = min(filter(lambda x: x%2 == 0, a))

ans = 0
ansm = 100000
for i in range(len(a)-2):
    k, l = a[i], a[i+2]
    h = a[i+1]
    if (k%2 == 0) + (l%2 == 0) == 1:
        if h % m == 0:
            ans += 1
            ansm = min(ansm, k+l)

print(ans, ansm)











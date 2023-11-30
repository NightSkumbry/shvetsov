
def f(n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return 1 + f(n-1)
    return f(n//2)


# for i in range(100):
#     print(i, f(i), bin(i)[2:].count('1')+1)

def F(n, m=1):
    if n == 1:
        return ['1', '0']
    
    ans = []
    for i in F(n-1, m):
        if i.count('1') == m:
            ans.append(i + '0')
        else:
            ans += [i+'0', i+'1']
    
    return ans

ans = 0
for i in range(1, 29):
    j = F(i)
    for i in j:
        if i.count('1') == 1 and int('1'+i, 2) <= 500_000_000:
            ans += 1
print(ans)



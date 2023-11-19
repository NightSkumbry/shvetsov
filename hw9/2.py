pr = []
for n in range(10, 100):
    for i in range(2, 1+int(n**0.5)):
        if n%i==0:
            break
    else:
        pr.append(n)

m = 0
mn = 0
for i in range(100, 1000):
    a = i//100
    b = i//10-10*a
    c = i%10
    ans = 0
    if a != 0:
        ans += sum((10*a+b in pr, 10*a+c in pr))
    if b != 0:
        ans += sum((10*b+a in pr, 10*b+c in pr))
    if c != 0:
        ans += sum((10*c+b in pr, 10*c+a in pr))
    if ans >= m:
        m = ans
        mn = i
print(mn)
        







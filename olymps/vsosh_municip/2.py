# 61

n = int(input())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

#min

m = (n//(a1+b2)) * a1
m += a1 * (n%(a1+b2) >= a1)
print(m, end=' ')

#max

m = (n//(a2+b1)) * a2
l = n%(a2+b1)
if l >= a2:
    m += a2
elif l >= a1:
    m += l
print(m)



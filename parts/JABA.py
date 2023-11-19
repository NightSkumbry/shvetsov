a = 'tytyyytytyyt'
x = 3 

# По условию нужно, что бы была минимальная длинна подстроки с x букв 't' в ней
ans = 10**10
c = [-10**10 for i in range(x - 1)]
ci = 0

for i, e in enumerate(a):
    if e == 't':
        ans = min(ans, i - c[ci % (x - 1)] + 1)
        c[ci % (x - 1)] = i
        ci += 1

print(ans)


# По условию нужно, что бы была минимальная длинна подстроки с x букв 't' в ней
ans = 0
c = [0 for i in range(x + 1)]
ci = 0

for i, e in enumerate(a):
    if e == 't':
        ans = max(ans, i - c[ci % (x + 1)] - 1)
        c[ci % (x + 1)] = i
        ci += 1

print(max(ans, i - c[ci % (x + 1)] - 1))
commands = [lambda x: x+1, lambda x: x*2]
n = [10]
end = 21


d = [0 for i in range(end)] + [1]

for i in range(end-1, 0, -1):
    if i in n:
        continue
    for c in commands:
        g = c(i)
        if g <= end:
            d[i] += d[g]
print(d[1], d)
            


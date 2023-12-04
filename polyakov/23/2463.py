cm = [lambda x: x+1, lambda x: x+3] # возможные команды
o = [2, 10, 20] # Начало, все обязательные, конец
n = [15] # Нельзя заходить

ans = 1
for ob in range(1, len(o)):
    d = [0 for i in range(o[ob]+1)]
    d[o[ob]] = 1
    for i in range(o[ob], o[ob-1]-1, -1):
        if i in n:
            continue
        for c in cm:
            g = c(i)
            if g <= o[ob]:
                d[i] += d[g]
    ans *= d[o[ob-1]]

print(ans)

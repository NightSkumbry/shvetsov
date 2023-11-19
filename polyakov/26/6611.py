with open('./files/26-125.txt') as f:
    a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[1:]))
    for i in range(len(a)):
        a[i][1] //= 2
    d = [-1 for _ in range(20)]
    a.sort(key=lambda x: x[0])

ans = 0
m = 0

for come_time in sorted(set(list(zip(*a))[0])):
    b = list(sorted(filter(lambda x: x[0] == come_time, a), key=lambda x: x[1]))
    for gnome in b:
        for cotel, time in enumerate(d):
            if gnome[0] >= time:
                et  = gnome[0]+gnome[1] + (2 * (time != -1))
                d[cotel] = et
                z = gnome[1] - (et-1440)*(et>1440)
                m = max(m, z)
                ans += z
                break

print(ans, m)

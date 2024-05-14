
with open('./files/24-280.txt') as f:
    a = f.read().lower().strip().replace('x', '1').replace('v', '1').replace('z', '1').split('1')


ans = 0
for q in a:
    l = 0
    ac = ec = ic = oc = uc = yc = 0
    for r in range(len(q)):
        if q[r] == 'a': ac += 1
        if q[r] == 'e': ec += 1
        if q[r] == 'i': ic += 1
        if q[r] == 'o': oc += 1
        if q[r] == 'u': uc += 1
        if q[r] == 'y': yc += 1
        while max(ac,ec,ic,oc,uc,yc) > 8:
            if q[l] == 'a': ac -= 1
            if q[l] == 'e': ec -= 1
            if q[l] == 'i': ic -= 1
            if q[l] == 'o': oc -= 1
            if q[l] == 'u': uc -= 1
            if q[l] == 'y': yc -= 1
            l+=1
        ans = max(ans, r-l+1)


print(ans)




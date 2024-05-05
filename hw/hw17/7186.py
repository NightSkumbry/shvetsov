
with open('./hw/hw17/26-143.txt') as f:
    N = int(f.readline())
    a = [list(map(int, i.split())) for i in f]
ml = 5
a.sort(key=lambda x: x[0])

q1 = []
q2 = []

ans1 = ans2 = 0

i = 0
ai = 0
while i <= a[-1][0] or (q1 or q2):
    if q1:
        q1[0] -= 1
        if q1[0] == 0:
            q1 = q1[1:]
            ans1 += 1
    if q2:
        q2[0] -= 1
        if q2[0] == 0:
            q2 = q2[1:]
    
    if a[ai][0] == i:
        c = 0
        if a[ai][2] == 1:
            if len(q1) < ml:
                c = 1
        if a[ai][2] == 2:
            if len(q2) < ml:
                c = 2
        if a[ai][2] == 0:
            if len(q1) <= len(q2) and len(q1) < ml:
                c = 1
            elif len(q2) < len(q1) and len(q2) < ml:
                c = 2
        
        if c == 0:
            ans2 += 1
        if c == 1:
            q1.append(a[ai][1])
        if c == 2:
            q2.append(a[ai][1])
        
        ai += 1
        if ai >= len(a):
            ai = 0
        
    i += 1


print(ans1, ans2)
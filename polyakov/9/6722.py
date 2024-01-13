from collections import Counter as C

with open('./files/9-222.csv') as f:
    a = [list(map(int, i.split(','))) for i in f]

for ind, i in enumerate(a):
    c = C(i)
    cm = c.most_common()
    if cm[0][1] == 2 and cm[1][1] == 1:
        if cm[0][0] >= (sum(i) - 2*cm[0][0])/4:
            print(ind+1)
            break
            







for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                k = (a <= b) and (not (b == c)) and (d <= a)
                if k:
                    print(a,b,c,d)

print('cdab')
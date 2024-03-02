
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                k = ((x <= w) or y and (not z)) and ((y <= (not z)) or x and (not w))
                if k == 0:
                    print(x, y, z, w)

print('zwyx')






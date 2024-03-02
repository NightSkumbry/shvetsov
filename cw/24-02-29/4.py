
def test(a):
    for x in range(200):
        for y in range(200):
            for z in range(200):
                k = (150 !=  y + 2*x + 2*z) or (a < x) or (a < y) or (a < z)
                if not k:
                    return False
    return True

from tqdm import tqdm
for a in tqdm(range(27, 10000)):
    if test(a):
        print(a)







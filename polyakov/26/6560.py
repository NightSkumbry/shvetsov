
with open('./files/26-123.txt') as f:
    a = f.raed().strip().split('\n')
    m = int(a[0].split()[0])
    a = list(map(lambda x: list(map(int, x.split())), a))
    

s = 0

ai = 0
for i in range(10000):
    







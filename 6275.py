with open('./files/24_6275.txt') as f:
    a = f.read().strip().lower()

ns = '0123456789abcdef'
n = {n:i for i, n in enumerate(ns)}
b = [0 for _ in range(len(ns))]
from queue import Queue as q
inds = q()

st = 0
m = 10**8

for i, e in enumerate(a):
    if e in ns:
        b[n[e]] += 1
        inds.put(i)
        if st == 0:
            st = i
        if all(b):
            while all(b):
                st = inds.get()
                b[n[a[st]]] -= 1
            m = min(m, i-st+1)

print(m)
                
                
    


from collections import Counter as C
from tqdm import tqdm

def F(file):
    with open(f'./files/27{file}_12413.txt') as f:
        N = int(f.readline())
        a = [int(i) for i in f]
    print(max(a), len(set(a)), N)
    
    c = C(a)
    ans = 0
    pc = 0
    for i in tqdm(c):
        p = c[i]*(c[i]-1)//2
        ans += pc*p + c[i]*(c[i]-1)*(c[i]-2)*(c[i]-3)//24
        pc += p
    print(ans)
        
        

F('A')
F('B')






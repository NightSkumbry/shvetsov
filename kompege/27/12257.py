from tqdm import tqdm

def F(file):
    with open(f'./files/27-{file}_12257.txt') as f:
        N = int(f.readline())
        a = [int(i) for i in f]

    k = 113
    
    b = [0] + [-1]*(k-1)
    b1 = [-1] + [-1]*(k-1)
    
    s = 0
    ans = l = 0
    for ind, i in tqdm(enumerate(a)):
        s += i
        if b[s%k] != -1:
            if s-b[s%k] > ans:
                l = ind-b1[s%k]
                ans = s-b[s%k]
            elif s-b[s%k] == ans:
                
                l = max(l, ind-b1[s%k])
          
        else:
            b[s%k] = s
            b1[s%k] = ind
        # print(l, ind-b1[s%k])
    print(l)


F('A')
F('B')


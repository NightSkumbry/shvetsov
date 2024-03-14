from tqdm import tqdm

def A(task):
    with open(f'./polyakov/variants/var_78258/27{task}.txt') as f:
        N = int(f.readline())
        a = [int(i) for i in f]
    
    ans = 0
    for i in tqdm(range(N)):
        sq = a[i]**0.5
        if a[i] % 21 == 0 and sq == int(sq):
            if int(sq) in a[i:]:
                ans = max(ans, N-a[::-1].index(sq)-i)
    print(ans)






A('A')
A('B')









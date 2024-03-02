from tqdm import tqdm

def A():
    with open('./yandex_edu/variants/597a2693-1f78-45be-8daf-d80e1f937a3d/27_B.txt') as f:
        n, k, r, t = map(int, f.readline().split())
        h = r*(k-t)
        a = [list(map(int, i.split())) for i in f]
        # print(a)
        # print(b)
        print(f'Оффисы: {n=}, Начальная T: {k=}, КМ -1Т: {r=}, Минимальная Т: {t=}')
    
    b = [0] * (10**6+4*h)
    
    for i in a:
        b[i[0]+2*h] = i[1]
    
    ans = 0
    for i in tqdm(range(10**6+4*h)):
        if b[i]:
            ans = max(ans, sum(b[i:i+h]), sum(b[i-h+1:i+1]))
            
    print(ans)


def B():
    with open('./yandex_edu/variants/597a2693-1f78-45be-8daf-d80e1f937a3d/27_T.txt') as f:
        n, k, r, t = map(int, f.readline().split())
        h = r*(k-t+1)
        a = [list(map(int, i.split())) for i in f]
        # print(a)
        # print(b)
        print(f'Оффисы: {n=}, Начальная T: {k=}, КМ -1Т: {r=}, Минимальная Т: {t=}')
    
    b = [0] * (10**6+4*h)
    
    for i in a:
        b[i[0]+2*h] = i[1]
    
    c = []
    for i in range(10**6+4*h):
        ...



A()











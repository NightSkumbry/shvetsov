#7c6369e8-bc02-4d5f-a0f8-a590afea969e

def F(file):
    with open(f'./yandex_edu/variants/7c6369e8-bc02-4d5f-a0f8-a590afea969e/27_{file}.txt') as f:
        K, N = map(int, f.readline().split())
        a = [int(i) for i in f]
    
    b = [0]*K
    for i in a:
        b.append(min(b[-K:]) + i)
    print(b[-1])

F('T')
F('A')
F('B')






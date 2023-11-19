import random

a = random.sample(range(1, 1000000), 100)
print(f'List: {a}, Count: {len(a)}')

def dels_count(n):
    a = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            a += 1
            a += 1 * (i == n//i)
    return a

b = list(zip(a, map(dels_count, a)))
b.sort(key=lambda x: x[1])
print(f'\n\nNumber: {b[-1][0]}, Del_count: {b[-1][1]}')

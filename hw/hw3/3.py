import random

a = random.sample(range(1, 10**10), 10**7)
print(f'Count: {len(a)}', f'\nList: {a}'*(len(a) <= 100))

def main():
    ts = 0
    tw = 0
    th = 0
    for i in a:
        if i % 26 == 0:
            ts += 1
            continue
        if i % 2 == 0:
            tw += 1
            continue
        if i % 13 == 0:
            th += 1
            continue
    print(f'\n\nAnswer: {ts*(len(a)-1) + tw*th}')
    

import timeit
print(f'Answering time: {timeit.timeit(main, number=1)} seconds')

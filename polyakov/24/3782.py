from collections import Counter as c
with open('./files/24-s1.txt') as f:
    a = f.read().strip().split('\n')
s = list(sorted([(i.count('Q'), i) for i in a]))[-1][1]
print(c(s).most_common()) # узнал интересующую букву
print(f'C{sum([i.count("C") for i in a])}')

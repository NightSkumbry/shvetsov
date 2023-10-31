with open('./files/26_10726.txt') as f:
    a = f.read().strip().split('\n')[1:]
    a = list(map(lambda x: list(map(int, x.split())), a))
    start, stop = zip(*a)

t = [0 for i in range(max(stop)+1)]
for b, e in a:
    for i in range(b, e):
        t[i] = 1
print(sum(t), max(map(len, ''.join(map(str, t)).split('0'))))
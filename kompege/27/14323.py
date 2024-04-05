
with open('./files/27-B_14323.txt') as f:
    N, M = map(int, f.readline().split())
    a = [int(i) for i in f]
    print(M, sum(a[:999]), a[999], a[998])

b = filter(lambda x: x<=1000, a)


def try_sum(su, sp, col=2):
    ...


c = 0
while b:
    s = 0
    i = -1
    while s + b[i] < M:
        s += b[i]
        i -= 1
    if M - s in b[:i]:
        c += 1
        b.remove(M-s)
        b = b[:i]
    else:
        i += 1
        s -= b[i]
        ts = try_sum(M-s, b[:i].copy())
        if not ts:
            input()




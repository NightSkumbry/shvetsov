alp = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def to_sys(n, a):
    r = ''
    while n > 1:
        r+=alp[n%a]
        n //= a
    r += alp[n%a] * (alp[n%a] != '0')
    return r[::-1]

for i in range(2, len(alp)):
    if to_sys(94, i)[:2] == '23':
        print(i)
        break

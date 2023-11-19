n = 1
al = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
}
while True:
    r = hex(n)[2:]
    if n % 2 == 0:
        r += 'f'
    else: 
        r += '0'
    
    r += hex(sum(map(lambda x: int(x, 16), r)) % 16)[2:]
    r += hex(sum(map(lambda x: int(x, 16), r)) % 16)[2:]
    d = [al[i] for i in r]
    if d.count(max(d)) == 5* d.count(min(d)):
        print(n)
        break

    n += 1
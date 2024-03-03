a = '0111111111111111112' + '2'*49 + '1'*94+ '0'
print(a.count('0'), a.count('2'), a.count('1'))
print(sum(map(int, a)))

while '00' not in a:
    b = a
    a = a.replace('02', '101', 1)
    a = a.replace('11', '2', 1)
    a = a.replace('012', '30', 1)
    a = a.replace('010', '00', 1)
    if a == b:
        break
else:
    print('legit')
print(a, sum(map(int, a)))


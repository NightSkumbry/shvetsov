a = '7'*200

while '7777' in a or '33333' in a:
    if '33333' in a:
        a = a.replace('33333', '777')
    else:
        a = a.replace('777', '33')

print(a.count('3'), a)
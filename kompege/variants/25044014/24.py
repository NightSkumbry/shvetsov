with open('./kompege/variants/25044014/24.txt') as f:
    print(max(map(len, f.read().strip().lower().replace('xzzy', 'xzz1zzy').split('1'))))




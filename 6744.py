for i in '0123456789abcdefghijklm':
    x = int(f'7{i}38596', 23)+int(f'14{i}36', 23)+int(f'61{i}7', 23)
    if x%22 == 0:
        print(x//22)
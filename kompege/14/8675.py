for i in '0123456789abcdef':
    x = int(f'1F3B{i}75', 16) + int(f'5D{i}3B', 16)
    if x%11 == 0:
        print(x//11)
# max
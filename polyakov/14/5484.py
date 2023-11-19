for i in '0123456789abcdefg':
    x = int(f'9759{i}', 17) + int(f'3{i}108', 17)
    if x%11 == 0:
        print(x//11)
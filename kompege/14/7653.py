for i in '0123456789abcdefghi':
    x = int(f'A3{i}74', 19) + int(f'{i}40846', 19)
    if x%9 == 0:
        print(x//9) 
# max
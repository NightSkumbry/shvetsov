for i in '123456789a':
    if int(f'3364{i}', 11) + int(f'{i}7946', 12) == int(f'55{i}87', 14):
        print(int(f'55{i}87', 14))
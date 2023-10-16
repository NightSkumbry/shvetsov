for i in '0123456789ABCDE':
    x = int(f'97968{i}13', 15) + int(f'7{i}213', 15)
    if x%14 == 0:
        print(x//14)
# min
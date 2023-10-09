with open('./files/26-125.txt') as f:
    a = list(map(int, f.read().strip().split()[2:]))
    d = 20
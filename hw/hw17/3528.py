
with open('./hw/hw17/24-153.txt') as f:
    a = f.read().strip().lower().replace('d', 'd1d').split('1')

print(min(filter(lambda x: x>2, map(len, a))))






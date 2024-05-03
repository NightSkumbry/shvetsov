
with open('./files/24-157.txt') as f:
    a = f.read().strip().lower().replace('qw', 'q1w').split('1')

print(max(map(len, a)))






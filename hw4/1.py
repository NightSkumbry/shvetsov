import random

a = random.sample(range(1, 1000000), 1000)
b = list(map(lambda x: sum(map(int, str(x))), a))
print(b.count(max(b)))
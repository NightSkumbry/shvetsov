import random
a = [random.randint(1, 1000) for _ in range(10000)]
# print(a)
print(max(map(len, ''.join(map(lambda x: str(int(len(str(x)) == 2)), a)).split('0'))))

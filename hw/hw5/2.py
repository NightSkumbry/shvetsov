nums = list(range(10))
laters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
import random
a = [random.choice(nums+laters) for _ in range(100000)]
print(max(map(len, ''.join(map(lambda x: str(int(x in nums)), a)).split('0'))))


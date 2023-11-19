import random

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

ans = 0
a = random.sample(range(1, 1000000), 1000)
b = list(map(is_prime, a))
for i in range(len(a)-1):
    ans += not ((b[i] + b[i+1] + 1)%3)

print(ans)
    

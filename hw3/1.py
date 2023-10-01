import random

a = random.sample(range(1, 1000000), 100)
print(f'Before: {a}, Count: {len(a)}')

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return True
    return False

b = list(filter(is_prime, a))

print(f'\n\nAfter: {b}, Count: {len(b)}')
print(f'\n\nDeleted: {set(a)-set(b)}')

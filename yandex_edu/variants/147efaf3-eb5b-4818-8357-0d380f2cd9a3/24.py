with open('./yandex_edu/variants/147efaf3-eb5b-4818-8357-0d380f2cd9a3/24.txt') as f:
    a = f.read().lower().strip().replace('ab', 'aabb').split('ab')

print(max(map(len, a)))
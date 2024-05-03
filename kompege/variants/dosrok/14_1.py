
a = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029

r = []
while a:
    r.append(a%27)
    a //= 27

ans = 0
for i in range(10, 27):
    ans += r.count(i)
print(ans)

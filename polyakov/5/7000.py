
ans = 0
# for n in range(100_000_000, 1_000_000_000):
#     s = sum(map(int, str(n)))
#     b = bin(s)[2:]
#     if b.count('1') == 0:
#         b = f'1{b}00'
#     else:
#         b = f'10{b}1'
#     if int(b, 2) == 21:
#         ans += 1

# print(ans)
# 21 = 10101 => подходит только else, с учётом, что сумма цифр равна 2. т. е. 8 штук (по 1 на каждый разряд) и 200_000_000
print(9)



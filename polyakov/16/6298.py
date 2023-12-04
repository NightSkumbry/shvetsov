def f(a, b):
    if b == 0:
        return a
    if a >= b:
        return f(a-b, b)
    return f(b, a)

# a = []
# for i in range(105):
#     if f(i, 105) == 1:
#         print(i)
#         a.append(i)
# print(a, len(a))
# print(200_000_000%105)
print(3 + 44 + (200_000_000-95 - 100_000_000+5)//105*48)

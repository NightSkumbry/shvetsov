def F(n):
    if n < 10:
        return n
    elif n%2 == 0:
        return F(n%10) + F(n//10)
    return F(10**n) + F(n%10) - 2

# 

def f(n):
    if n < 10:
        return n
    elif n%2 == 0:
        # return сумма цифр после последней нечётной цифры + f(n до последней нечетной)
        pass
    else:
        return n%10 - 1
# ноль возможен тоько если последняя нечётная цифра в числе равна 1, а все после неё - нули
# таким образом у нас есть 9 двузначных чисел оканчивающихся на 1, но 9*10 если учесть всевозможные нули на конце
# 90 трёхзначных, но 90*9 с нулями и тд
ans = 0
for i, j in enumerate(range(10, 0, -1)):
    ans += int('9'+'0'*i)*j
print(ans)


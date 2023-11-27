def f(n):
    if n == 0:
        return 6
    if n % 2 == 0:
        return 1 + f(n//2)
    return f(n//2)

# данная функция считает количесво нулей в двоичной записи числа и прибавляет 6
# значит нас интересуют числа, с тремя нулями

def f(n, m): # Данная функция вернёт все возможные строки из 1 и 0, длинной n, в которых <= m нулей
    if n == 1:
        return ['1', '0']
    ans = []
    for i in f(n-1, m):
        if i.count('0') == m:
            ans += [i+'1']
        else:
            ans += [i+'1', i+'0']
    return ans

ans = 0
for i in range(3, 30):
    d = len(list(filter(lambda x: x.count('0') == 3 and int('1' + x[::-1], 2) <= 1_000_000_000, f(i, 3))))
    print(i, d)
    ans += d
print(ans)


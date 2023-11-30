
def f(n):
    if n <= 1:
        return n
    if n%3 == 0:
        return n + f(n//3)
    return n + f(n+3)

# Если число на 3 не делится, то функция улетает в бесконечность, так как прибавление тройки не изменит этого
# Значит, изначальное число должно быть кратно трём
# Одноко, если число делится на три, но при делении на три даёт число не делящееся на 3, то
# это тоже улетит в бесконечность.
# Для того, что бы было определено нужно число - степень тройки
# Теперь про смысл возвращаемых данных, это сумма всех степеней тройки, до n
# 27 - не достаточно, а 81 достаточно
print(81)






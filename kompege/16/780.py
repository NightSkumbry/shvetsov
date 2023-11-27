import functools
@functools.lru_cache(None) # Хрен его знает чт это, но оно ожевило код
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 2*f(1-n)+3*f(n-1)+2
    return -f(-n)

# Обрати внимание, сделано в германии!, то есть в задаче сказано найти сумму цифр в искомом числе
print(sum(map(int, str(f(50))))) 

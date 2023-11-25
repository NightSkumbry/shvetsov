# 10

d, n = map(int, input().split())
 
if n == 0:
    print(str(d+1), str(d+1))
elif n < 10:
    if d == 0:
        print(0, (n-1)*10)
    else:
        print(str(d)*n, str(d)*n)
elif n == 10:
    if d == 0:
        print(0, (n-1)*10)
    else:
        print(f'{d}1', f'{d}9')

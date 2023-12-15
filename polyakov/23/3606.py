
def f(n, stop, j=0):
    if n == stop:
        return True
    if n > stop or j == 5:
        return False
    return f(n+1, stop, j+1) or f(n*2, stop, j+1) or f(n+n%4, stop, j+1)

ans = 0
for i in range(100):
    ans += f(i, 80)


print(ans)


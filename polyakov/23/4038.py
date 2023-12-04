c = [lambda x: x+1, lambda x: x*2+1]

def f(n, e):
    if e == 0:
        return [n]
    ans = []
    for i in c:
        ans += f(i(n), e-1)
    return ans
        
print(len(set(f(3, 11))))
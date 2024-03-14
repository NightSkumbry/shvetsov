
def f(n):
    if n == 0:
        return 0 
    if n % 2 == 0:
        return f(n//2) + 3
    return 2*f(n-1) + 1

a = set()
for n in range(1, 1001):
    a.add(f(n))
print(len(a))












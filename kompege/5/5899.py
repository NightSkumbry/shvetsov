prs = 0
n = 1000
def is_prime(n):
    n = int(n)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(999, 99, -1):
    i = str(i)
    ns = [i[0]+i[1], i[0]+i[2]]
    if i[1] != 0:
        ns += [i[1]+i[2], i[1]+i[0]]
    if i[2] != 0:
        ns += [i[2]+i[1], i[2]+i[0]]
    ns = sum(map(is_prime, ns))
    if ns > prs:
        n = i
        prs = ns

print(n)
        
    
    
    
    

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

k = 1
for i in range(2943444, 2943529+1):
    if is_prime(i):
        print(k, i)
        k+=1
        
        






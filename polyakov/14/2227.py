a = abs(9**7 + 3**21 - 8)
p = ''
while a > 0:
    p+=str(a%3)
    a//=3
    
print(sum(map(int, p)))
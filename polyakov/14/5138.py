import re
a = abs(19**81 + 23**709 - 4)
p = ''
while a > 0:
    p+=str(a%9)
    a//=9
print(len(re.findall(r'8[1-7]', p[::-1])))

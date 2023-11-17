with open('./files/24-j3.txt') as f:
    a = f.read().lower()
print(a.count('tok') + a.count('tik'))
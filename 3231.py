
def v(n):
    ans = 0
    for i in range(g+1):
        ans += i * a[(i+n)%len(a)]
        ans += i * a[(-i+n)%len(a)]
    ans -= g * a[(g+n)%len(a)] * (len(a)%2 == 0)
    return ans



with open('./files/27-A_3231.txt') as f:
    a = list(map(int, f.read().strip().split('\n')[1:]))
g = len(a)//2
a3 = [2*a[i]-a[(i+g)%len(a)]-a[(i-g)%len(a)] for i in range(len(a))]
a1 = [v(0), v(1)]
a2 = [a1[1]-a1[0]]
for i in a3[1:]:
    a2.append(a2[-1]+i)
for i in a2[1:-1]:
    a1.append(a1[-1]+i)

print(a1.index(min(a1))+1)
# print(list(map(lambda x: v(x[0]), enumerate(a))), a1, a2, a3, sep='\n')

with open('./files/27-B_3231.txt') as f:
    a = list(map(int, f.read().strip().split('\n')[1:]))
g = len(a)//2
a3 = [2*a[i]-a[(i+g)%len(a)]-a[(i-g)%len(a)] for i in range(len(a))]
a1 = [v(0), v(1)]
a2 = [a1[1]-a1[0]]
for i in a3[1:]:
    a2.append(a2[-1]+i)
for i in a2[1:-1]:
    a1.append(a1[-1]+i)

print(a1.index(min(a1))+1)



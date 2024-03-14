
def A():
    with open('./files/27-133a.txt') as f:
        n = int(f.readline())
        a = [int(i) for i in f]

    ans = 0
    for i in range(len(a)):
        for j in a[i+1:]:
            if (a[i]+j)%4 == 0:
                if (a[i]*j)%2187 == 0:
                    ans += 1
    print(ans)


A()

def f37(n):
    ans = 0
    while ans < 7 and n%3 == 0:
        ans += 1
        n//=3
    return ans

def B():
    with open('./files/27-133b.txt') as f:
        n = int(f.readline())
        a = [int(i) for i in f]
    fours = [[0]*8 for _ in range(4)]
    
    ans = 0
    
    for i in range(1, n):
        j = i-1
        i = a[i]
        j = a[j]
        fours[j%4][f37(j)] += 1
        ans += sum(fours[(4-(i)%4)%4][7-f37(i):])
    
    print(ans)
    

B()








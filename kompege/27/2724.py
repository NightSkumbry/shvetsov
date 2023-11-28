def A():
    with open('./files/27A_2724.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    ans = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[j] + a[i]) % 131 == 0:
                ans += 1

    print(ans)


def B():
    with open('./files/27B_2724.txt') as f:
        a = list(map(int, f.read().strip().split('\n')[1:]))
    k = [0 for i in range(131)]
    for i in a:
        k[i%131] += 1

    ans = 0
    for i in a:
        k[i%131] -= 1
        ans += k[(131-i%131)%131]

    print(ans)


import timeit
print(timeit.timeit(A, number=1))
print(timeit.timeit(B, number=1))





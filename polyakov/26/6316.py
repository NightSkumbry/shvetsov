with open('./files/26-111.txt') as f:
    a = list(map(lambda x: list(map(int, x.split())), f.read().strip().split('\n')[2:]))
    a.sort(key=lambda x: x[0])
    d = [-1 for _ in range(210)]
# print(a[:2])

ans = 0
m = (0, 0) # last_visit, cage

for came_time in sorted(set(list(zip(*a))[0])):
    b = list(filter(lambda x: x[0] == came_time, a))
    b.sort(key=lambda x: x[1])
    for passenger in b:
        for cage, emp_time in enumerate(d):
            if passenger[0] > emp_time:
                d[cage] = passenger[1]
                ans += 1
                if m[0] != passenger[0]:
                    m = (passenger[0], cage+1)
                break
print(ans, m[1])
    

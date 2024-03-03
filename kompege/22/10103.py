
a = list(zip('''4
3
5
7
6
2
5
2
7
8
6
6'''.split(), [list(map(lambda x: int(x)-1, i.split(';'))) if i != '0' else [] for i in '''0
0
1;2
3
3
5
4;6
7
0
0
9
10'''.split()]))
times = []
depends = []
can_be_parallel = [set(range(len(a)))-set(map(lambda x: x-1, i)) for i in [
    {3,4,5,6,7,8},
    {3,4,5,6,7,8}, 
    {2,1,5,6,4,7,8},
    {3,1,2,7,8},
    {3,1,2,6,7,8},
    {5,3,1,2,7,8},
    {8,4,6,5,3,1,2},
    {7,6,5,4,3,2,1},
    {11},
    {12},
    {9},
    {10},
]]


z = set()
for i in a:
    z.update(set(i[1]))
    depends.append(set(i[1]))
    times.append(int(i[0]))
nz = set(range(len(a))) - z


def update_depends(n):
    for i in a[n][1]:
        update_depends(i)
        depends[n].update(depends[i])
for i in nz:
    update_depends(i)
print(depends)


from itertools import permutations


def run(running, processes, not_started):
    res = running[0]
    r = 0
    if not not_started:
        return res
    running = list(map(lambda x: x-res, running[1:]))
    processes = processes[1:]
    for i in not_started:
        prov = can_be_parallel[i] & can_be_parallel[processes[0]] & can_be_parallel[processes[1]] & can_be_parallel[processes[2]]
        if i in prov and processes[0] in prov and processes[1] in prov and processes[2] in prov:
            runn, proc = map(list, zip(*sorted(zip(running+[times[i]], processes+[i]))))
            not_s = not_started - ({i}|depends[i])
            r = max(r, run(runn, proc, not_s))
    return res + r
    
ans = 0
for p1, p2, p3, p4 in permutations(range(len(a)), 4):
    prov = can_be_parallel[p1] & can_be_parallel[p2] & can_be_parallel[p3] & can_be_parallel[p4]
    if p1 in prov and p2 in prov and p3 in prov and p4 in prov:
        t = 0
        not_started = set(range(len(a))) - (depends[p1]|depends[p2]|depends[p3]|depends[p4]|{p1,p2,p3,p4})
        running = sorted([times[i] for i in (p1, p2, p3, p4)])
        processes = sorted([p1, p2, p3, p4], key=lambda x: times[x])
        f = run(running, processes, not_started)
        if f > ans:
            ans = f
        
print(ans)





# for first in range(len(a)):
#     not_started = set(range(len(a))) - depends[first]
#     can_be_used = can_be_parallel[first] & not_started
#     if len(can_be_used) < 3:
#         continue
    
#     for second in can_be_used:
#         not_started -= {second} | depends[second]
#         can_be_used &= can_be_parallel[second] & not_started
#         if len(can_be_used) < 2:
#             continue
        
#         for third in can_be_used:
#             not_started -= {third} | depends[third]
#             can_be_used &= can_be_parallel[third] & not_started
#             if len(can_be_used) < 1:
#                 continue
            
#             for fourth in can_be_used:
#                 not_started -= {fourth} | depends[fourth]
#                 proc = sorted([first, second, third, fourth], key=lambda x: times[x])
                
                







count = 13
times = [97,149,44,80,26,47,74,82,137,90,48,84,17]
depends = [
    set(),
    set(),
    {0,1},
    {0,1,2},
    {0,1,2},
    {0,1,2,4},
    {0,1,2,3,4,5},
    set(),
    set(),
    {7,8},
    {7,8,9},
    {7,8,9},
    {7,8,9,10}
]
can_be_parallel = [
    {0,1,8,9,10,11,12},
    {1,0,8,9,10,11,12},
    {2,8,9,10,11,12},
    {3,4,5,8,9,10,11,12},
    {4,3,8,9,10,11,12},
    {5,3,8,9,10,11,12},
    {6,8,9,10,11,12},
    {7},
    {8,0,1,2,3,4,5,6},
    {9,0,1,2,3,4,5,6},
    {10,11,0,1,2,3,4,5,6},
    {11,10,12,0,1,2,3,4,5,6},
    {12,11,0,1,2,3,4,5,6}
]

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
for p1, p2, p3, p4 in permutations(range(count), 4):
    prov = can_be_parallel[p1] & can_be_parallel[p2] & can_be_parallel[p3] & can_be_parallel[p4]
    if p1 in prov and p2 in prov and p3 in prov and p4 in prov:
        t = 0
        not_started = set(range(count)) - (depends[p1]|depends[p2]|depends[p3]|depends[p4]|{p1,p2,p3,p4})
        running = sorted([times[i] for i in (p1, p2, p3, p4)])
        processes = sorted([p1, p2, p3, p4], key=lambda x: times[x])
        f = run(running, processes, not_started)
        if f > ans:
            ans = f
        
print(ans)



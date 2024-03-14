from itertools import product
ans = set()
for i in product(['а', 'в', 'и', 'к', 'п', 'р', 'ч', 'ы'], repeat=5):
    ans.add(''.join(i))
ans = sorted(ans)
k = 0
for i in range(len(ans)):
    if (i + 1) % 5 == 0:
        k+=1
        continue
    if len(set(ans[i])) == 5:
        if all([l in 'вкпрч' for l in ans[i]]):
            print(i+1-k)
            break


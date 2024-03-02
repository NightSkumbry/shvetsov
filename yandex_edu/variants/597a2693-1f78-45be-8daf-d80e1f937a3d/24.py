with open('./yandex_edu/variants/597a2693-1f78-45be-8daf-d80e1f937a3d/24.txt') as f:
    a = f.read().strip()

import re
f = re.findall(r'((?:y[a4]nd[e3]x)*((y[a4]nd[e3]x)|(y[a4]nd[e3])|(y[a4]nd)|(y[a4]n)|(y[a4])|(y))?)', a)

print(max(map(lambda x: len(x[0]), f)))
    
    
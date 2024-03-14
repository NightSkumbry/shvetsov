from re import fullmatch
from tqdm import tqdm

for i in tqdm(range(0, 10**9, 13)):
    if str(i)[0] != '2':
        continue
    if fullmatch(r'24[02468]*68[39]35', str(i)):
        print(i, i//13)












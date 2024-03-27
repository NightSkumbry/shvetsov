from tqdm import tqdm
with open('./files/24_14242.txt') as f:
    a = f.read().strip().lower().replace('3', '1').replace('2', '0').replace('d', 'b').replace('e', 'a')

r = {
    (0, 0): 0,
}

ch = 0
gl = 0

ans = 0

for i, e in tqdm(enumerate(a)):
    match e:
        case '0':
            ch += 1
        case '1':
            ch -= 1
        case 'b':
            gl -= 1
        case 'a':
            gl += 1
    
    if (ch, gl) in r.keys():
        ans = max(ans, i+1-r[(ch, gl)])
    else:
        r[(ch, gl)] = i+1

print(ans)




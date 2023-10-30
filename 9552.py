with open('./files/24_9552.txt') as f:
    a = f.read().strip().lower().replace('pcsgo', 'csgo')
import re
print(max(map(lambda x: len(x[0]), re.findall(r'(((pc)|(csgo))+)', a))))
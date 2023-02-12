from os import listdir
from os.path import isfile, join

text_dct = {}
text_name_list = [f for f in listdir() if f.endswith(".txt") and isfile(join(f))]

for el in text_name_list:
    with open(f'{el}', 'r', encoding='utf-8') as f:
        text = []
        k = 0
        for row in f:
            k += 1
            t = row.strip().split('\n')
            text.extend(t)
        text.insert(0, k)
        text_dct[el] = text

sorted_dict = dict(sorted(text_dct.items(), key=lambda item: item[1]))
print(sorted_dict)

with open(f'end_file.txt', 'w', encoding='utf-8') as f:
    for key in sorted_dict.keys():
        f.write(f'{key}\n')
        for el in sorted_dict[key]:
            f.write(f'{el}\n')


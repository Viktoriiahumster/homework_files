text_dct = {}

for i in range(1, 4):
    text_name = f'{i}.txt'
    with open(text_name, 'r', encoding='utf-8') as f:
        text_dct[text_name] = sum(1 for line in f)

max_t = text_dct.get(max(text_dct, key=text_dct.get))
min_t = text_dct.get(min(text_dct, key=text_dct.get))
max_file = f'{list(text_dct.keys())[list(text_dct.values()).index(max_t)]}'
min_file = f'{list(text_dct.keys())[list(text_dct.values()).index(min_t)]}'
second_t = ''


with open('end_file.txt', 'w', encoding='utf-8') as f:
    f.write(f'{max_file}\n')
    f.write(f'{max_t}\n')
with open(f'{max_file}', 'r', encoding='utf-8') as f_f, open('end_file.txt', 'a', encoding='utf-8') as f:
    for line in f_f:
        f.write(line)
    f.write('\n')
with open('end_file.txt', 'a', encoding='utf-8') as f:
    for value in text_dct.values():
        if value < max_t and value > min_t:
            second_t = f'{list(text_dct.keys())[list(text_dct.values()).index(value)]}'
            f.write(f'{second_t}\n')
            f.write(f'{value}\n')
with open(f'{second_t}', 'r', encoding='utf-8') as f_f, open('end_file.txt', 'a', encoding='utf-8') as f:
    for line in f_f:
        f.write(line)
    f.write('\n')
with open('end_file.txt', 'a', encoding='utf-8') as f:
    f.write(f'{min_file}\n')
    f.write(f'{min_t}\n')
with open(f'{min_file}', 'r', encoding='utf-8') as f_f, open('end_file.txt', 'a', encoding='utf-8') as f:
    for line in f_f:
        f.write(line)
    f.write('\n')
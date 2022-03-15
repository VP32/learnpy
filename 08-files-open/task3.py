import os.path

files = [
    '1.txt',
    '2.txt',
    '3.txt'
]

filedata = []

for file in files:
    with open(os.path.join("sorted", file), 'rt', encoding='utf-8') as f:
        lines = f.readlines()
        filedata.append({'name': file, 'lines_count': len(lines), 'lines': lines})

filesorted = sorted(filedata, key=lambda d: d['lines_count'])

with open('joined.txt', 'w', encoding='utf-8') as f:
    for file in filesorted:
        f.write(f'{file["name"]}\n')
        f.write(f'{file["lines_count"]}\n')
        f.writelines(file['lines'])
        f.write('\n')
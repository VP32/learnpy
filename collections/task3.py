queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

queries_count = len(queries)
words_count_data = {}

for query in queries:
    words = query.split(' ')
    key = len(words)

    if key not in words_count_data.keys():
        words_count_data.setdefault(key, {'count': 1})
    else:
        words_count_data[key]['count'] = words_count_data[key]['count'] + 1

for k, v in words_count_data.items():
    words_count_data[k].setdefault('distribution', round(100 * words_count_data[k]['count'] / queries_count, 2))
    print('Количество слов: {}, процент {} %'.format(k, words_count_data[k]['distribution']))

print(words_count_data)

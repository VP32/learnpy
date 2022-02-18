boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()

    for pair in zip(boys, girls):
        print(f'{pair[0]} vs {pair[1]}')
else:
    print('Не совпадает количество М и Ж!  Кто-то может остаться без пары!')

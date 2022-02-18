stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_rating_name = ''
max_rating = 0

for data in stats.items():
    if data[1] > max_rating:
        max_rating = data[1]
        max_rating_name = data[0]

print(max_rating_name)

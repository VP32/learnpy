initial_list = ['2018-01-01', 'yandex', 'cpc', 100]
initial_list.reverse()

result_dict = initial_list[0]

for item in initial_list[1:]:
    result_dict = {item: result_dict}

print(result_dict)

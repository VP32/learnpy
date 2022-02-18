height = 182
age = 19
children_count = 0
is_learning = False

if 18 < age < 27:
    if children_count < 2:
        if not is_learning:
            if height < 170:
                print('В танкисты')
            elif height < 180:
                print('На флот')
            elif height < 200:
                print('В десантники')
            else:
                print('В другие войска')
        else:
            print('Отсрочка по учебе')
    else:
        print('Отсрочка по детям')
else:
    print('Непризывной возраст')
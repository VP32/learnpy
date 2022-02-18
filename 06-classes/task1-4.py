class Goose:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Гагага'

    def speak(self):
        return self.voice

    def feed(self):
        print("Мнямням")

    def collect_eggs(self):
        print("Яйца собраны")


class Cow:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Муууууууу!'

    def speak(self):
        return self.voice

    def feed(self):
        print("Мнямням")

    def milk(self):
        print("Подоено")


class Sheep:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Беееее!'

    def speak(self):
        return self.voice

    def feed(self):
        print("Мнямням")

    def cut(self):
        print("Стрижка проведена")


class Chicken:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Кудкудах!'

    def speak(self):
        return self.voice

    def feed(self):
        print("Мнямням")

    def collect_eggs(self):
        print("Яйца собраны")


class Goat:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Меееее!'

    def speak(self):
        return self.voice

    def feed(self):
        print("Мнямням")

    def milk(self):
        print("Подоено")


class Duck:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Кря!'

    def speak(self):
        return self.voice

    def feed(self):
        print("Мнямням")

    def collect_eggs(self):
        print("Яйца собраны")


animals = []
animals.append(Goose('Серый', 4))
animals.append(Goose('Белый', 3))
animals.append(Cow('Манька', 50))
animals.append(Sheep('Барашек', 31))
animals.append(Sheep('Кудрявый', 31))
animals.append(Chicken('Ко-Ко', 3))
animals.append(Chicken('Кукареку', 2.5))
animals.append(Goat('Рога', 13))
animals.append(Goat('Копыта', 14))
animals.append(Duck('Кряква', 2.8))

max_weight = 0
max_weight_name = None

for animal in animals:
    print(f'Животное {animal.name} говорит {animal.speak()}')
    animal.feed()
    if isinstance(animal, Cow) or isinstance(animal, Goat):
        animal.milk()
    if isinstance(animal, Sheep):
        animal.cut()
    if isinstance(animal, Duck) or isinstance(animal, Chicken) or isinstance(animal, Goose):
        animal.collect_eggs()

    if animal.weight > max_weight:
        max_weight = animal.weight
        max_weight_name = animal.name


print(f'Животное с максимальным весом: {max_weight_name}, вес: {max_weight}')
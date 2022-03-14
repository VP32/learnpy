class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = ''

    def feed(self):
        print("Мнямням")

    def speak(self):
        return self.voice


class Milkable(Animal):
    def milk(self):
        print("Подоено")


class Woodable(Animal):
    def cut(self):
        print("Стрижка проведена")


class Bird(Animal):
    def collect_eggs(self):
        print("Яйца собраны")


class Goose(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Гагага'


class Cow(Milkable):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Муууууууу!'


class Sheep(Woodable):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Беееее!'


class Chicken(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Кудкудах!'


class Goat(Milkable):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Меееее!'


class Duck(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Кря!'


animals = [Goose('Серый', 4), Goose('Белый', 3), Cow('Манька', 50), Sheep('Барашек', 31), Sheep('Кудрявый', 31),
           Chicken('Ко-Ко', 3), Chicken('Кукареку', 2.5), Goat('Рога', 13), Goat('Копыта', 14), Duck('Кряква', 2.8)]

max_weight = 0
max_weight_name = None

for animal in animals:
    print(f'Животное {type(animal).__name__} {animal.name} говорит {animal.speak()}')
    animal.feed()
    if isinstance(animal, Milkable):
        animal.milk()
    if isinstance(animal, Woodable):
        animal.cut()
    if isinstance(animal, Bird):
        animal.collect_eggs()

    if animal.weight > max_weight:
        max_weight = animal.weight
        max_weight_name = animal.name

print(f'Животное с максимальным весом: {max_weight_name}, вес: {max_weight}')

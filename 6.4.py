class Car:
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if int(self.speed) > 60:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if int(self.speed) > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car = input('Type of car(town/sport/work/police): ')
speed_info, color_info, name_info = input('Введите скорость автомобиля: '), input('Введите цвет автомобиля: '), input(
    'Введите название автомобиля: ')
if car == 'town':
    car = TownCar(speed_info, color_info, name_info)
elif car == 'sport':
    car = SportCar(speed_info, color_info, name_info)
elif car == 'work':
    car = WorkCar(speed_info, color_info, name_info)
elif car == 'police':
    car = PoliceCar(speed_info, color_info, name_info)

car.go()
car.stop()
car.turn(input('В каком направлении поворачивает? '))
car.show_speed()

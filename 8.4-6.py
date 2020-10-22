# не понял особо смысла задания и времени было очень немного, поэтому сделал всё по минимуму, извиняюсь

class EquipmentWarehouse:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unit = {
            'Наименование устройства': self.name,
            'Цена за единицу': self.price,
            'Количество': self.quantity
        }
        self.warehouse = []

    def new_product(self):
        while input('Добавляем товар? да/нет ') == 'да':
            try:
                unit = input(f'Введите наименование устройства ')
                unit_p = int(input(f'Введите цену за единицу '))
                unit_q = int(input(f'Введите количество '))
                unit = {'Наименование устройства': unit, 'Цена за единицу': unit_p, 'Количество': unit_q}
                self.unit.update(unit)
                self.warehouse.append(self.unit)
                print(f'Текущий список устройств на складе -\n {self.warehouse}')
            except ValueError:
                print('Данные введены неверно')

    def move_product(self):
        name = input('Какой товар перемещаем? ')
        place = input('Куда перемещаем? ')
        for i in self.warehouse:
            if name in i.values():
                print(f'Устройства {name} перевезены в {place}')
            else:
                print('Устройства не найдены.')


class Printer(EquipmentWarehouse):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


class Scanner(EquipmentWarehouse):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


class Xerox(EquipmentWarehouse):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


a = Printer('XP', 1000, 15)
a.new_product()
a.move_product()

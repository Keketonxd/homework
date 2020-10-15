class Worker:
    
    def __init__(self, name, surname, position):
        def position_check(pos):
            if pos == 'работник':
                return {'wage': 20, 'bonus': 10}
            elif pos == 'менеджер':
                return {'wage': 30, 'bonus': 20}
            elif pos == 'директор':
                return {'wage': 500, 'bonus': 100}  # так можно делать?)
            else:
                return {'wage': 0, 'bonus': 0}

        self.name = name
        self.surname = surname
        self.position = position
        self._income = position_check(position)


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(sum(v for v in self._income.values()))


a = Position(input('Введите имя: '), input('Введите фамилию: '),
             input('Введите должность(работник/директор/менеджер): '))
a.get_full_name()
a.get_total_income()

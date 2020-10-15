class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        if self.title:
            print(f'Запуск отрисовки. Инструмент: {self.title}.')
        else:
            print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title='ручка'):
        super().__init__(title)


class Pencil(Stationery):
    def __init__(self, title='карандаш'):
        super().__init__(title)


class Handle(Stationery):
    def __init__(self, title='маркер'):
        super().__init__(title)


a = Pen()
b = Pencil()
c = Handle()

a.draw()
b.draw()
c.draw()

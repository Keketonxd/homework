class Clothes:
    def __init__(self, type, size_or_height):
        self.type = type
        self.size = int(size_or_height)

    @property
    def cloth_amount(self):
        if self.type == 'пальто':
            return round(self.size / 6.5 + 0.5, 2)
        elif self.type == 'костюм':
            return 2 * self.size + 0.3


a = Clothes(input('Тип одежды(пальто/костюм): '), input('Размер для пальто или высота для костюма: '))
print(a.cloth_amount)

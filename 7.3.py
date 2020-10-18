class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        return self.quantity - other.quantity if self.quantity > other.quantity else f'Вторая клетка больше'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, in_row):
        string = ''
        for i in range(self.quantity // in_row):
            string += '*' * in_row + '\n'
        string += '*' * (self.quantity % in_row)
        return string


cell = Cell(48)
cell_2 = Cell(30)
print(cell + cell_2)
print(cell - cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell.make_order(15))

class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input('Введите делимое: ')
divisor = input('Введите делитель: ')

try:
    if int(divisor) == 0:
        raise DivisionByZero('Делить на ноль нельзя!')
    print(round(int(dividend) / int(divisor), 2))
except ValueError:
    print('Введите числа!')
except DivisionByZero as err:
    print(err)

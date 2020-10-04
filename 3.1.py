def division(dividend, divisor):
    return dividend / divisor


try:
    print(division(float(input('Введите делимое: ')), float(input('Введите делитель: '))))
except ZeroDivisionError:
    print('На ноль делить нельзя!!!')
except ValueError:
    print('Вводите числа.')

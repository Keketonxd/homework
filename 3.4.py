import math


def my_func(x, y):
    if x <= 0 or y >= 0:
        raise ValueError
    return round(x ** y, 4)


# def my_func_2(x, y):
#    if x <= 0 or y >= 0:
#        raise ValueError
#    z = x
#    for i in range(1, abs(y)):
#        z *= z
#    return round(1 / z, 4)


try:
    print(my_func(float(input('Введите действительное положительное число: ')),
                  int(input('Введите целое отрицательное число: '))))
except ValueError:
    print('Вы ввели числа, не соблюдая указанные условия')

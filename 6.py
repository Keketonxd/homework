print('Каждый день спортсмен пробегал на 10% больше километров, чем в предыдущий.')
a = int(input('Сколько он пробежал в первый день: '))
b = int(input('Какова его цель: '))
i = 1
while a < b:
    a *= 1.1
    i += 1
print(f'Спортсмен достигнет своей цели на {i}-й день')
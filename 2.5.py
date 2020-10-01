numbers = [7, 5, 3, 3, 2]
print(f'Начальный рейтинг: {numbers}')
answer = ''
while answer.lower() != 'нет':
    try:
        numbers.append(int(input('Введите целое число: ')))
    except ValueError:
        print('Да, всё таки это должно быть целое число.')
    numbers = sorted(numbers, reverse=True)
    print(numbers)
    answer = input('Продолжаем добавлять числа? ("нет" для выхода) ')

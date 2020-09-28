revenue = int(input('Какова выручка фирмы: '))
costs = int(input('Каковы издержки фирмы: '))
profit = revenue - costs
if profit < 0:
    print('Фирма работает в убыток.')
elif profit == 0:
    print('Вы выходите в ноль.')
else:
    print('Поздравляем, фирма приносит прибыль!')
    print(f'Рентабельность вашей фирмы составляет {profit/revenue}')
    workers = int(input('Сколько в вашей фирмы рабочих: '))
    print(f'В среднем, один рабочий приносит Вам {profit/workers} чистой прибыли.')

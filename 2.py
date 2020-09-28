seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600  # поскольку в часе 3600 секунд
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60
print(f'Мы перевели время в часы, минуты и секунды, получили: {hours}:{minutes}:{seconds}')

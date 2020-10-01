
def what_month_list(month):
    if 1 <= month <= 13:
        months_list = []
        for i in range(1, 13):
            months_list.append(i)
        if 3 <= month <= 5:
            print('весна')
        elif 6 <= month <= 8:
            print('лето')
        elif 9 <= month <= 11:
            print('осень')
        else:
            print('зима')
    else:
        raise Exception


def what_month_dict(month):
    months_dict = {}
    for i in range(1, 13):
        if 3 <= i <= 5:
            months_dict[i] = 'весна'
        elif 6 <= i <= 8:
            months_dict[i] = 'лето'
        elif 9 <= i <= 11:
            months_dict[i] = 'осень'
        else:
            months_dict[i] = 'зима'
    print(months_dict[month])


try:
    what_month_list(int(input('Какой месяц если смотреть по списку? ')))
except Exception:
    print('В следующий раз напишите номер месяца от 1 до 12')


try:
    what_month_dict(int(input('Какой месяц если смотреть по словарю? ')))
except Exception:
    print('В следующий раз напишите номер месяца от 1 до 12')

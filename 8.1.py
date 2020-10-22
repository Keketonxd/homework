class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def to_numeric(cls, date):  # долго думал, не надумал ничего интереснее(
        day = int(date.split('.')[0])
        month = int(date.split('.')[1])
        year = int(date.split('.')[2])
        return f'{day:02}.{month:02}.{year:04}'

    @staticmethod
    def check_date(day, month, year):
        print(a.to_numeric(f'{day}.{month}.{year}'))
        if 0 > day or day > 32:
            return 'Неправильный день'
        elif 0 > month > 12:
            return 'Неправильный месяц'
        else:
            return 'Всё в порядке)'


a = Data('11.10.1998')
print(a.check_date(42, 2, 4))
print(a.to_numeric('12.15.1321'))

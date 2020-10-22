class ListValueError(Exception):
    def __init__(self, txt):
        self.txt = txt


final_lst = []
gg = False

while not gg:
    alarm = False
    lst = input('Введите числа и строки, разделённые пробелом. Для остановки введите q. ')
    try:
        if lst == 'q':
            gg = True
        lst = lst.split()
        for i in lst:
            if i.isdigit():
                final_lst.append(float(i))
            else:
                alarm = True
        if alarm:
            raise ListValueError('В списке остаются только числа.')
    except ListValueError as err:
        print(err)
        
print(final_lst)

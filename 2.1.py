a = [1.3, (1, 2, {'why': None}, True, 'abc'), {1, 2, None, True, 'abc'}, {'name': 'Ark', 'age': 21, 'is cool': True},
     'abc']

for i in range(len(a)):
    print(f'{i + 1}-й элемент списка - {type(a[i])}')

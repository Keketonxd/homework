with open('5.1.txt', 'w', encoding='utf-8') as f:
    user_input = ' '
    while user_input:
        user_input = input('Введите данные: ')
        f.write(user_input + '\n')

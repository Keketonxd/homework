number = int(input('Введите число: '))
max_digit = 0
while number > 10:
    check = number % 10
    number //= 10
    if check > max_digit:
        max_digit = check
print(f'Максимальная цифра в числе :{max_digit}')

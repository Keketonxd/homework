from random import randint

with open('5.5.txt', 'w+', encoding='utf-8') as f:
    for i in range(randint(5, 20)):
        next_num = randint(-100, 100)
        f.write(f'{next_num} ')
    f.seek(0)
    numbers = f.read().split()
    total = 0
    for number in numbers:
        number = int(number)
        total += number
    print(total)

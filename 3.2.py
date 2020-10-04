def information(**kwargs):
    for i in kwargs:
        print(kwargs[i], end=" ")


information(name=input('Ваше имя: '), surname=input('Ваша фамилия: '), date_of_birth=input('Ваша дата рождения: '),
            city_of_birth=input('Ваш город рождения: '), email=input('Ваш email: '),
            phone=input('Номер телефона: '))

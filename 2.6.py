goods = []
number = 1
final_dict = {}

while input("Добавляем продукт? да/нет: ") == 'да':
    good = {}
    while input("Добавляем характеристики продукта? да/нет: ") == 'да':
        good_key = input("Введите характеристику товара: ")
        good_value = input("Введите значение характеристики товара: ")
        good[good_key] = good_value
    goods.append(tuple([number, good]))
    number += 1

print(goods)
for good in goods:
    for good_key, good_value in good[1].items():
        if good_key in final_dict:
            final_dict[good_key].append(good_value)
        else:
            final_dict[good_key] = [good_value]
print(final_dict)

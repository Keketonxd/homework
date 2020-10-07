from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


# def fact_2(n):
#     count = 1
#     for i in range(1, n + 1):
#         count *= i
#         yield count
#
#
# for el in fact_2(int(input('Факториал какого числа вы хотели бы получить: '))):
#     print(el)

for el in fact(int(input('Факториал какого числа вы хотели бы получить: '))):
    print(el)

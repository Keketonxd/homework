from itertools import count, cycle


def iterator_a(n, max_num):
    for el in count(n):
        if el > max_num:
            break
        else:
            print(el)


def iterator_b(foo, foo_count):
    c = 0
    for el in cycle(foo):
        if c >= foo_count * len(foo):
            break
        print(el)
        c += 1


iterator_a(int(input('С какого числа начинаем: ')), int(input('До какого числа шагаем: ')))
iterator_b(input('Какую строку будем повторять: '), int(input('Сколько раз будем её повторять: ')))

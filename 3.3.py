def my_func(a, b, c):
    lst = [a, b, c]
    lst_min = min(lst)
    return a + b + c - lst_min


print(my_func(
    int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))

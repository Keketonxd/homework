do_it = True
end_sum = 0


def addition(numbers):
    global end_sum, do_it
    pre_sum = numbers.split()
    for i in range(len(pre_sum)):
        try:
            end_sum += float(pre_sum[i])
        except ValueError:
            do_it = False
            break
    print(end_sum)


while do_it:
    addition(input('Введите строку чисел, разделенных пробелом \nДля отсновки сложения введите не число: '))

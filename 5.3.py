with open('5.3.txt', encoding='utf-8') as f:
    my_dict = {}
    my_lst = []
    total_salary = 0
    for line in f:
        lst = line.split()
        my_dict[lst[0]] = int(lst[1])
    for k, v in my_dict.items():
        total_salary += my_dict[k]
        if v < 20000:
            my_lst.append(k)
    print(my_lst)
    print(round(total_salary / len(my_dict), 2))

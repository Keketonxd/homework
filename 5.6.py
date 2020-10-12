with open('5.6.txt', encoding='utf-8') as f:
    my_dict = {}
    for line in f:
        total = 0
        for i in line.split()[1:]:
            num = (''.join(x for x in list(i) if x.isdigit()))
            try:
                total += int(num)
            except ValueError:
                continue
        my_dict[line.split()[0]] = total
    print(my_dict)

import json

lst = []
with open('5.7.txt', 'r', encoding='utf-8') as f, open('5.7_2.txt', 'w', encoding='utf-8') as f_2:
    my_dict = {}
    avg_profit = 0
    count = 0
    for line in f:
        profit = int(line.split()[2]) - int(line.split()[3])
        my_dict[line.split()[0]] = profit
        avg_profit += profit
    the_end = [my_dict, {'avg_profit': avg_profit / len(my_dict)}]
    json.dump(the_end, f_2)
# делал впопыхах за 10 мин до дедлайна, сори)()

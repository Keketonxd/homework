with open('5.2.txt', encoding='utf-8') as f:
    content = f.readline()
    count = 0
    while content:
        print(len(content.split()))
        count += 1
        content = f.readline()
    print(f'Количество строк: {count}')

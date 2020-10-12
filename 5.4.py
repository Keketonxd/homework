translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('5.4.txt', encoding='utf-8') as old, open('5.4_2.txt', 'w', encoding='utf-8') as new:
    for line in old:
        symbols = line.split()
        symbols[0] = translator.get(symbols[0])
        new.write(' '.join(symbols) + '\n')

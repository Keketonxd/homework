words = input('Введите строку из нескольких слов, разделённых пробелами: ')
for ind, el in enumerate(words.split()):
    print(f'{ind + 1}) {el:.10}')

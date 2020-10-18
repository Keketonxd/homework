class Matrix:
    lst = None

    def __init__(self, lists):
        self.lst = lists

    def __str__(self):
        string = ''
        for i in self.lst:
            string += f'{i}\n'
        return string

    def __add__(self, other):
        string = ''
        for i in range(len(self.lst)):
            for j in range(len(self.lst[i])):
                string += f'{self.lst[i][j] + other.lst[i][j]} '
            string += '\n'
        # for i, j in self.lst, other.lst:
        #     for x in range(len(i)):
        #        string += f'{i[x] + j[x]} '  # не понимаю, почему j[0], к примеру, это 3, должен быть 5?
        #     string += '\n'
        return string


try:
    a = Matrix([[1, 2, 3], [3, 4, 5]])
    b = Matrix([[5, 6, 7], [7, 8, 9]])
    print(a + b)
except Exception as ex:
    print(f'Что-то ввели неправильно, {ex}')

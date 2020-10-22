class ComplexNumber:
    num = None
    complex_num = None

    def __init__(self, num, complex_num):
        self.num = num
        self.complex_num = complex_num

    def __add__(self, other):
        return f'{self.num + other.num} + {self.complex_num + other.complex_num}i'

    def __mul__(self, other):
        real = self.num * other.num - self.complex_num * other.complex_num
        comp = self.num * other.complex_num + other.num * self.complex_num
        return f'{real} + {comp}i '


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
print(a + b)
print(a * b)

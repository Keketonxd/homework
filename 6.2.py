class Road:
    __length = None
    __width = None

    def __init__(self):
        self.__length = 15
        self.__width = 20

    def account(self, mass, thickness):
        return mass * thickness * self.__length * self.__width


r = Road()
print(r.account(int(input('Масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: ')),
                int(input('Число см толщины полотна: '))))

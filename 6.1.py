import time


class TrafficLight:
    colour = None

    def running(self, seconds):
        if seconds <= 0:
            raise ValueError
        for i in range(seconds):
            if 0 <= i % 18 < 7:
                self.colour = 'красный'
            elif 7 <= i % 18 < 10:
                self.colour = 'жёлтый'
            else:
                self.colour = 'зелёный'
            print(f'Горит {self.colour}.')
            time.sleep(1)


a = TrafficLight()
try:
    a.running(int(input('Сколько секунд работает светофор? ')))
except ValueError:
    print('Введите натуральное число')
# зелёный горит 8 секунд

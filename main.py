class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds) % 60
        h = (self.seconds // 3600) % 24
        return f'{h:02}:{m:02}:{s:02}'

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self
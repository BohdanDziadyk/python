from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __add__(self, other):
        p1 = self.a + self.b + self.c
        p2 = other.a + other.b + other.c
        return sqrt(p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.c)) + sqrt(
            p2 * (p2 - other.a) * (p2 - other.b) * (p2 - other.c))

    def __sub__(self, other):
        p1 = self.a + self.b + self.c
        p2 = other.a + other.b + other.c
        return sqrt(p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.c)) - sqrt(
            p2 * (p2 - other.a) * (p2 - other.b) * (p2 - other.c))

    def __eq__(self, other):
        p1 = self.a + self.b + self.c
        p2 = other.a + other.b + other.c
        return sqrt(p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.c)) == sqrt(
            p2 * (p2 - other.a) * (p2 - other.b) * (p2 - other.c))

    def __ne__(self, other):
        p1 = self.a + self.b + self.c
        p2 = other.a + other.b + other.c
        return sqrt(p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.c)) != sqrt(
            p2 * (p2 - other.a) * (p2 - other.b) * (p2 - other.c))

    def __gt__(self, other):
        p1 = self.a + self.b + self.c
        p2 = other.a + other.b + other.c
        return sqrt(p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.c)) > sqrt(
            p2 * (p2 - other.a) * (p2 - other.b) * (p2 - other.c))

    def __lt__(self, other):
        p1 = self.a + self.b + self.c
        p2 = other.a + other.b + other.c
        return sqrt(p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.c)) < sqrt(
            p2 * (p2 - other.a) * (p2 - other.b) * (p2 - other.c))

    def __len__(self):
        return self.a + self.b + self.c


list_1 = []


class Letter:
    __count = 0

    def __init__(self):
        self.__count += 1
        self.__text = ''

    def get_text(self):
        return self.__text

    def set_text(self, value):
        self.__text = value

    @classmethod
    def print_count(cls):
        print(cls.__count)

    def text_append(self):
        list_1.append(self.__text)


letter = Letter()
letter = Letter()
letter = Letter()
letter.print_count()
letter.set_text("biba")
print(letter.get_text())
letter.text_append()
print(list_1)

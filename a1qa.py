import math
from operator import itemgetter


class Triangle(object):

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def square(self):
        s = 0.5 * ((self.first[0]-self.third[0])*(self.second[1]-self.third[1])-(self.second[0]-self.third[0])*(self.first[1]-self.third[1]))
        print("Площадь треугольника = ", abs(s))

    def check_koor(self):
        dct = {}

        for value in [self.first, self.second, self.third]:
            dot = math.sqrt(int(value[0])*int(value[0]) + int(value[1])*int(value[1]))
            a = tuple(value)
            dct[a] = dot
        print("Ближайшая точка к началу координат ",
              (sorted(dct.items(), key=itemgetter(1)))[0][0])

    def angle(self):
        a = self.first
        b = self.second
        c = self.third
        AB = (b[0]-a[0], b[1]-a[1])
        AC = (c[0]-a[0], c[1]-a[1])
        BA = (a[0]-b[0], a[1]-b[1])
        BC = (c[0]-b[0], c[1]-b[1])
        CA = (a[0]-c[0], a[1]-c[1])
        CB = (b[0]-c[0], b[1]-c[1])
        try:
            ABAC = (AB[0] * AC[0] + AB[1] * AC[1]) /\
                   (math.sqrt(AB[0] ** 2 + AB[1] ** 2) * math.sqrt(AC[0] ** 2 + AC[1] ** 2))
        except ZeroDivisionError:
            ABAC = 0
        try:
            BABC = (BA[0] * BC[0] + BA[1] * BC[1]) / \
                   (math.sqrt(BA[0] ** 2 + BA[1] ** 2) * math.sqrt(BC[0] ** 2 + BC[1] ** 2))
        except ZeroDivisionError:
            BABC = 0
        try:
            CACB = (CA[0] * CB[0] + CA[1] * CB[1]) / \
                   (math.sqrt(CA[0] ** 2 + CA[1] ** 2) * math.sqrt(CB[0] ** 2 + CB[1] ** 2))
        except ZeroDivisionError:
            CACB = 0
        LABAC = math.acos(ABAC)*(180/math.pi)
        LBABC = math.acos(BABC)*(180/math.pi)
        LCACB = math.acos(CACB)*(180/math.pi)
        if LABAC == 90.0:
            print("Угол с координатами {} прямой".format(a))
        elif LBABC == 90.0:
            print("Угол с координатами {} прямой".format(b))
        elif LCACB == 90.0:
            print("Угол с координатами {} прямой".format(c))
        else:
            print("Прямых углов нет")


def read_file(file_name):
    with open(file_name, "r") as f:
        data = list()
        for str_line in f.readlines():
            line = list()
            for dot in str_line.split():
                x, y = dot.split(',')
                line.append((int(x.strip()), int(y.strip())))
            data.append(line)

        return data


def main():
    data = read_file('1.txt')
    for triangle in data:
        tri = Triangle(triangle[0], triangle[1], triangle[2])
        tri.check_koor()
        tri.square()
        tri.angle()
        print(" ")


if __name__ == '__main__':
    main()

import math
from operator import itemgetter


class Triangle(object):
    first = (0, 0)
    second = (0, 0)
    third = (0, 0)

    def __init__(self, file_name):
        self.file_name = file_name


    def square(self):
        s = 0.5 * ((self.first[0]-self.third[0])*(self.second[1]-self.third[1])-(self.second[0]-self.third[0])*(self.first[1]-self.third[1]))
        print(s)

    def check_koor(self, ):
        dct = {}

        for value in [self.first, self.second, self.third]:
            dot = math.sqrt(int(value[0])*int(value[0]) + int(value[1])*int(value[1]))
            a = tuple(value)
            dct[a] = dot
        print((sorted(dct.items(), key=itemgetter(1)))[0][0])

    def open_file(self):
        with open(self.file_name, "r") as f:
            data = list()
            for str_line in f.readlines():
                line = list()
                for item in str_line.split(','):
                    line.append(int(item.strip()))
                data.append(line)
            self.first = data[0]
            self.second = data[1]
            self.third = data[2]


def main():
    tri = Triangle('1.txt')
    tri.open_file()
    tri.check_koor()
    tri.square()
    print(tri.first, tri.second)

if __name__ == '__main__':
    main()

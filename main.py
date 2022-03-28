import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def num_print(self):
        if self.imag is 0:
            print(self.real)
        elif self.real is 0:
            print(str(self.imag) + 'i')
        else:
            print(str(self.real) + '+' + str(self.imag) + 'i')

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def __sub__(self, other):
        return Complex(
            self.real - other.real,
            self.imag - other.imag
        )

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        r = (self.real * other.real + self.imag * other.imag) / (other.real * other.real + other.imag * other.imag)
        i = (self.imag * other.real - self.real * other.imag) / (other.real * other.real + other.imag * other.imag)
        return Complex(r, i)

    def length(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)



    #def __pow__(self, power):


    a = 5
    print(f'{a} hello')








p1 = Complex(3, 2)
p2 = Complex(4, 0)

p3 = p1 + p2
p3.num_print()

print(p2.length())

print(f'{p2}')
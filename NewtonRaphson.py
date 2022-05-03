from prettytable import PrettyTable
from math import cos, sin

class NetwonRaphson:

    def __init__(self, x0):
        self.x = x0
        self.x_new = 0
        self.i = 1
        self.output = PrettyTable(["No. of iteration",f"x{self.i}", f"f(x{self.i})", f"f'(x{self.i})", f"x{self.i + 1}"])
        self.iteration()

    def eq(self, x):
        self.f = round(x ** 3 - 2, 6)
        self.f_dash = round(3 * (x ** 2), 6)

    def processing(self):
        self.eq(self.x)
        self.x_new = round(self.x - (self.f/self.f_dash), 5)

    def iteration(self):
        while True:
            self.processing()
            self.output.add_row([self.i, self.x, self.f, self.f_dash, self.x_new])
            if self.x_new == self.x:
                break
            self.x = self.x_new
            self.i += 1
        print(self.output)

x0 = 2
newton = NetwonRaphson(x0)
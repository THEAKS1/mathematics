from prettytable import PrettyTable
from math import exp, cos

class Secant:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = 1
        self.output = PrettyTable(["No. of iteration", "x[n]", "x[n+1]", "x[n+2]"])
        self.iterating()

    def eq(self, x):
        # Type your equation here
        result = (x * exp(x)) - cos(x)     #<-- Equation
        return result

    def processing(self):
        self.x_new = ((self.a * self.eq(self.b)) - (self.b * self.eq(self.a))) / (self.eq(self.b) - self.eq(self.a))
        self.x_new = round(self.x_new, 3)

    def iterating(self):
        while True:
            self.processing()
            self.output.add_row([self.i, self.a, self.b, self.x_new])
            if self.x_new == self.b:
                break
            self.a, self.b = self.b, self.x_new
            self.i += 1
        print(self.output)


# Enter your interval here in the format [a,b]
a = 0   # Lower Limit
b = 1   # Upper Limit
bm = Secant(a, b)
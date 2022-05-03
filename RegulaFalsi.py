from prettytable import PrettyTable
from math import exp, cos

class RegulaFalsi:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = 0
        self.output = PrettyTable(["No. of iteration","Interval", "Approximated Value", "f(Approximated Value)", "+ve or -ve"])
        self.iterating()

    def eq(self, x):
        # Type your equation here
        result = (x ** 4) - x - 9    #<-- Equation
        return result

    def processing(self, x):
        result = self.eq(x)
        if result == 0:
            print(self.output)
            print("Ans: ", x)
            exit()
        elif result > 0:
            self.output.add_row([self.i,f"[{self.a}, {self.b}]", x, result, "Positive"])
            if self.eq(self.a) < 0:
                self.b = round(x, 4)
            else:
                self.a = round(x, 4)
        else:
            self.output.add_row([self.i,f"[{self.a}, {self.b}]", x, result, "Negative"])
            if self.eq(self.a) < 0:
                self.a = round(x, 4)
            else:
                self.b = round(x, 4)

    def iterating(self):
        while self.eq(self.b) - self.eq(self.a) != 0:
            self.i += 1
            regula = ((self.a * self.eq(self.b)) - (self.b * self.eq(self.a))) / (self.eq(self.b) - self.eq(self.a))
            regula = round(regula, 4)
            if round(self.b, 3) == round(regula, 3) or round(self.a, 3) == round(regula, 3):
                self.processing(regula)
                break
            self.processing(regula)
        print(self.output)
        print("Ans: ", round(regula, 3))

# Enter your interval here in the format [a,b]
a = 1   # Lower Limit
b = 2   # Upper Limit
bm = RegulaFalsi(a, b)
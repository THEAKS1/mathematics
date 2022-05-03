from prettytable import PrettyTable
from math import log10

class BisectionMethod:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = 0
        self.output = PrettyTable(["No. of iteration","Interval", "Mid Value", "f(mid value)", "+ve or -ve"])
        self.iterating()

    def eq(self, x):
        # Type your equation here
        result = (x ** 3) - 5 * x + 1     #<-- Equation
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
        while round(self.a, 3) != round(self.b, 3):
            self.i += 1
            mid = (self.a + self.b) / 2
            mid = round(mid, 4)
            self.processing(mid)
        print(self.output)
        print("Ans: %.4f"%self.a)

# Enter your interval here in the format [a,b]
a = 0   # Lower Limit
b = 1   # Upper Limit
bm = BisectionMethod(a, b)
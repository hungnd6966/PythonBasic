class Fraction:
    def __init__(self, n = 0 , d = 1):
        self.numerator = n
        self.denominator = d

    def input(self):
        frac_input = raw_input()
        self.numerator = frac_input.split('/')[0]
        self.denominator = frac_input.split('/')[1]

    def show(self):
        print(str(self.numerator) + "/" + str(self.denominator))

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_value(self, n, d):
        self.numerator = n
        self.denominator = d

    def evaluate(self):
        return float(self.numerator)/float(self.denominator)
    

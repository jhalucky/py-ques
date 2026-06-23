class Fraction:

    def __init__(self,num,den): #parameterized constructor
        self.numerator = num
        self.denominator = den
        
    

    def __add__(self, other):
        new_num = self.numerator*other.denominator + other.numerator*self.denominator
        new_den = self.denominator*other.denominator
        return '{}/{}'.format(new_num, new_den)

    def __str__(self):
        return '{}/{}'.format(self.numerator,self.denominator) # "{self.numerator}/{self.denominator} will also work but it will not give the output in the form of fraction, it will give the output in the form of string"
    








obj1 = Fraction(2,9)
print(type(obj1))
obj2 = Fraction(3,9)
print(obj1, obj2)
print(obj1 + obj2)
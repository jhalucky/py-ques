class Rectangle:

    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        area = self.length * self.height
        return area
    
    def is_square(self):
        if self.length == self.height:
            return True
        else:
            return False
        



rect1 = Rectangle(10,10)
rect2 = Rectangle(10,20)
print(rect1.is_square())
print(rect1.area())
print(rect2.is_square())
print(rect2.area())


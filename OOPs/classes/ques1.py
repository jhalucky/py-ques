class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        self.perimeter = 2 * (self.length + self.width)
        return self.perimeter
    

    def Area(self):
        self.area = self.length * self.width
        return self.area
    
    def display(self):

        # here we are calling these methods cuz if we don't call these methods they won't return area or perimeter till then, we tried calling display() method without calling Area() and Perimeter()
        # it was throwing error, either call these methods in display() or call it while creating obj but calling method is important
        self.Perimeter() 
        self.Area()
        return f"Length of rectangle: {self.length}\nWidth of Rectangle: {self.width}\nPerimeter od Rectangle: {self.perimeter}\nArea of Rectangle: {self.area}"
    





rect1 = Rectangle(10,20)
print(f"Area of rectangle: {rect1.Area()}")
print(f"Perimeter of rectangle: {rect1.Perimeter()}") 
print(rect1.display())
class Coordinate:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # self.origin = ''
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    
    def points(self,other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        return f"coord1: ({self.x},{self.y}), coord2: ({other.x}, {other.y})"
    
    def distance(self, other):
        x1 = self.x
        x2 = other.x
        y1 = self.y
        y2 = other.y
        distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        return distance
    
    def distance_from_origin(self):
        x1 = 0
        y1 = 0
        x2 = self.x
        y2 = self.y
        distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        return distance
        

    def distance(cls, obj1, obj2):
        x1 = obj1.x
        x2 = obj2.x
        y1 = obj1.y
        y2 = obj2.y
        distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        return distance



obj1 = Coordinate(1,2)
obj2 = Coordinate(0,0)
print(type(obj1))
distance1 = Coordinate.distance(obj1, obj2)
distance2 = Coordinate.distance_from_origin(obj1)
print(obj1, obj2)
print(distance1, distance2)
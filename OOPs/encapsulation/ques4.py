class Student:

    def __init__(self, student_id, marks, age):

        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def validate_marks(self):

        if self.__marks < 0 or self.__marks > 100:
            return False
        
        else:
            return True
        

    def validate_age(self):

        if self.__age > 20:
            return True
        
        else:
            return False
        

    
    def check_qualifications(self):

       if self.validate_marks() and self.validate_age():
           if self.__marks >= 65:
               return True
           
           else:
               return False


       else:
           return False

       
        








stu1 = Student(23456789, 25, 20)
stu2 = Student(29876450, 65, 21 )
print(stu1. validate_marks())
print(stu1.validate_age())
print(stu1.check_qualifications())



print(stu2. validate_marks())
print(stu2.validate_age())
print(stu2.check_qualifications())

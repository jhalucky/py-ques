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
       


    def display(self):
            
        return f"Student Id: {self.__student_id}\nMarks: {self.__marks}\nAge: {self.__age}\nQualified: {self.check_qualifications()} "

       
        








stu1 = Student(23474500, 25, 20)
stu2 = Student(29874501, 65, 21)
stu3 = Student(29874502, 25, 22)
stu4 = Student(29874503, 95, 18)
stu5 = Student(29874504, 55, 25)

# print(stu1. validate_marks())
# print(stu1.validate_age())
# print(f"Candiadte Report: {stu1.check_qualifications()}")



# print(stu2. validate_marks())
# print(stu2.validate_age())
# print(f"Candidate Report: {stu2.check_qualifications()}")
print(stu1.display())
print(stu2.display())
print(stu3.display())
print(stu4.display())
print(stu5.display())
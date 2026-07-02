class Student:

    def __init__(self):

        self.__student_id = None
        self.__marks = None
        self.__age = None
    
    def set_student_id(self, student_id):
        self.__student_id = student_id
    
    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age
    

    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return self.__age

    def validate_marks(self):

        # if self.__marks < 0 or self.__marks > 100: we can use this way also
        if self.get_marks() < 0 or self.get_marks() > 100:  #using getter method
            return False
        
        else:
            return True
        

    def validate_age(self):

        # if self.__age > 20:
        if self.get_age() > 20:
            return True
        
        else:
            return False
    

    
    def check_qualifications(self):

       if self.validate_marks() and self.validate_age():
           if self.get_marks() >= 65:
               return True
           
           else:
               return False


       else:
           return False
       


    def display(self):
            
        return f"Student Id: {self.__student_id}\nMarks: {self.get_marks()}\nAge: {self.get_age()}\nQualified: {self.check_qualifications()} "

       
        








stu1 = Student()
stu1.set_student_id(29874500)
stu1.set_marks(25)
stu1.set_age(20)
print(stu1.display())

# stu2 = Student(29874501, 65, 21) when not using setter method
# stu3 = Student(29874502, 25, 22)
# stu4 = Student(29874503, 95, 18)
# stu5 = Student(29874504, 55, 25)


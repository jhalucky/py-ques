# class User:

#     def __init__(self):
#         self.name = 'Lucky'
#     def login(self):
#         print('Login here')


# class Student(User):

#     # def __init__(self, roll_no):
#     #     self.roll_no = roll_no

#     def enroll(self):
#         print('Enroll for courses')

# # name = 'Lucky'
# u = User()
# s = Student()
    
# print(s.name)
# # print(s.roll_no)
# s.login()
# s.enroll()


class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    

class Child(Parent):

    def __init__(self, num, val):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val


c = Child(100,200)
print(c.get_num())
print(c.get_val())



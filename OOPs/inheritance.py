class User:

    def __init__(self):
        self.name = 'Lucky'
    def login(self):
        print('Login here')


class Student(User):

    # def __init__(self, roll_no):
    #     self.roll_no = roll_no

    def enroll(self):
        print('Enroll for courses')

# name = 'Lucky'
u = User()
s = Student()
    
print(s.name)
# print(s.roll_no)
s.login()
s.enroll()
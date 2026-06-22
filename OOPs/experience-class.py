class Experience:

    def __init__(self):
        self.qualification = ''
        self.programme = ''
        self.yearsOfExperinence = ''
        self.info()
    
    def info(self):
        name = input("Enter your name: ")
        age = int(input("Enter age: "))
        qualifications = input("Enter your qualifications: ")
        qualifications = self.qualification
        programme = input("Enter your programme: ")
        programme = self.programme
        email = input("Enter your mail id: ")
        contact_no = int(input("Enter Contact No: "))
        yearsOfExperience = int(input("Enter no. of years experience: "))
        self.yearsOfExperinence = yearsOfExperience


        
        if yearsOfExperience == 0:
            self.experience()
        elif yearsOfExperience == 1:
            self.experience()
        elif yearsOfExperience == 2:
            self.experience()
        elif yearsOfExperience == 3:
            self.experience()
        elif yearsOfExperience == 4:
            self.experience()
        else:
            print("Doesn't matter how many years of experience you have, we need one year more experience than you have!")


    def experience(self):
        print(f" '{self.yearsOfExperinence + 1} years Experience needed' ")



obj = Experience()
    

        


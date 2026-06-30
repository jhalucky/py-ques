class Instructor:

    def __init__(self, name, experience, technical_skills, average_feedback):
        self.__name = name
        self.__experience = experience
        self.__technical_skills =  technical_skills
        self.__average_feedback = average_feedback


    def check_eligibility(self):
        if self.__experience > 3 and self.__average_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__average_feedback >= 4:
            return True
        
        else:
            return False
        

    def allocate_course(self, technology):
        if technology in self.__technical_skills:
            return True
        else:
            return False
        


inst1 = Instructor("Lucky", 5, ["Python", "Java", "SQL", "C++"], 5)
print(inst1.check_eligibility())
print(inst1.allocate_course("Rust"))

from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):
        print("Connected to Database")
    
    @abstractmethod
    def security(self):
        print("Its very important to secure any application!")


class MobileApp(BankApp):

    def mobile_login(self):
        print("Login Here!")


    # Here if want to inherit an abstract class, we have to create a method in the child class with same method name as in parent class, for this it is security

    def security(self):
        return super().security()
    



class WebApp(BankApp):

    def web_login(self):
        print("Login on website!")


    def security(self):
        return super().security()

    



obj1 = MobileApp()
obj2 = WebApp()
obj1.database()
obj1.security()
obj1.database()
obj1.mobile_login()

obj2.security()
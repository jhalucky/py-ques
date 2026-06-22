class Atm:

    def __init__(self):
        self.pin = ''
        self.balance = 1024356
        self.menu()


    def menu(self):

        while True: 

            user_input = input(
            """"
            Hey man! how may i help you?
            1. Press 1 to Create Pin
            2. Press 2 to Change the pin
            3. Press 3 to Check balance
            4. Press 4 to withdraw cash
            5. Press 5 to exit
            """
        )


            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.change_pin()
            elif user_input == '3':
                self.check_balance()
            elif user_input == '4':
                self.withdraw_cash()
           


    def create_pin(self):
        user_pin = input("Enter 6 digits to create a pin: ")
        confirmed_pin = input("Enter pin again: ")
        

        if confirmed_pin == user_pin:
            self.pin = user_pin
            print("Pin created Successfully!")

        else:
            print("Pin does not match")



    def change_pin(self):
        if self.pin == "":
            print("Create a pin first!")
            return 
            
        existing_pin = input("Enter existing pin: ")

        if existing_pin == self.pin:
            new_pin = input("Enter new pin: ")
            confirm_pin = input("confirm new pin: ")

            if new_pin == confirm_pin:
                self.pin = new_pin   
                print('Pin changed successfully!')
            else:
                print("PIN configuration failed")

        else:
            print("Existing pin doesn't match!")



    def check_balance(self):
        if self.pin == "":
            print("Create a pin first!")
            return self.create_pin()

        existing_pin = input("Enter pin: ")

        if existing_pin == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid pin!")
   

    def withdraw_cash(self):
        pin = input("Enter your pin: ")
        if pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            print("Receive Cash From Below!")
            balance_left = self.balance - amount
            print(f"Balance Left in: {balance_left}")

        else:
            print("Incorrect Pin!")


obj = Atm()

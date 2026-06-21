class Atm:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()


    def menu(self):
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
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            pass


    def create_pin(self):
        user_pin = int(input("Enter 6 digits to create a pin: "))
        confirmation_pin = int(input("Enter pin again: "))

        if confirmation_pin == user_pin:
            print("Pin created Successfully!")

        else:
            print("Pin does not match")



obj = Atm()

class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"name: {self.name}\nGender: {self.gender}\nAddress: {self.address}"
        # return f"{self.address.house_address}, {self.address.landmark}, {self.address.__city}, {self.address.pincode}, {self.address.state}"



class Address:

    def __init__(self, house_address, landmark, city, pincode, state):
        self.house_address = house_address
        self.landmark = landmark
        self.__city = city
        self.pincode = pincode
        self.state = state

    def __str__(self):
        return f"{self.house_address}, {self.landmark}, {self.__city}, {self.pincode}, {self.state}"


add1 = Address('E-117, Harkesh Nagar, Okhla Phase-2, Okhla Industrial Estate', 'Near Bal Vaishali Public School', 'New Delhi', 110020, 'Delhi')
cust1 = Customer('Lucky Jha', 'Male', add1)
# cust1.address()
# print(add1)
print(cust1)
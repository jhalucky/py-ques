class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"name: {self.name}\nGender: {self.gender}\nAddress: {self.address}"
        # return f"{self.address.house_address}, {self.address.landmark}, {self.address.__city}, {self.address.pincode}, {self.address.state}"


    def edit_profile(self,new_name,new_address):
        self.name = new_name
        self.address = new_address
        return f"name: {self.name}\nGender: {self.gender}\nAddress: {self.address}"




class Address:

    def __init__(self, house_address, landmark, city, pincode, state):
        self.house_address = house_address
        self.landmark = landmark
        self.city = city
        self.pincode = pincode
        self.state = state

    def __str__(self):
        return f"{self.house_address}, {self.landmark}, {self.city}, {self.pincode}, {self.state}"

    def edit_address(self, new_house_address, new_landmark, new_city, new_pincode, new_state):
        self.house_address = new_house_address
        self.landmark = new_landmark
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state



add1 = Address('E-117, Harkesh Nagar, Okhla Phase-2, Okhla Industrial Estate', 'Near Bal Vaishali Public School', 'New Delhi', 110020, 'Delhi')
cust1 = Customer('Lucky Jha', 'Male', add1)
# cust1.address()
# print(add1)
add2  = Address('E-118, Ismailpur, Okhla Phase-2, Okhla Industrial Estate', 'Near Cheel', 'Faridabad', 110020, 'Haryana')
cust2 = Customer('Priya Sharma', 'Female', add2)

new_address = Address(
    "Sector-15",
    "Near Metro Station",
    "Gurugram",
    122001,
    "Haryana"
)

add1.edit_address('E-117, Harkesh Nagar, Okhla Phase-2, Okhla Industrial Estate', 'Near Valmiki Mandir', 'New Delhi', 110020, 'Delhi')
cust1.edit_profile('Aryan Jha', add1)
print(f"Customer 1:\n{cust1}")
print(f"Customer 2:\n{cust2}")
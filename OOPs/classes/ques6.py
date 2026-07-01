class Car:

    instance_count = 0

    def __init__(self, make, model):
        Car.instance_count += 1
        self.make = make
        self.model = model

        print(f"Created a {self.make} {self.model} Car instance.")

    @classmethod      #if we hadn't used this keyword here, we wouldn't able to access Car.get-instance_count(), still we can access it using obj name but using @classmethod keyword is correct way of coding.
    def get_instance_count(self):

        return self.instance_count
    

maruti = Car("Maruti", "Swift")
hyundai = Car("Hyundai", "Creta")
honda = Car("Honda", "City")
print(f"Total no of Car instance created: {Car.get_instance_count()}")
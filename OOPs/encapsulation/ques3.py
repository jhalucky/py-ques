# Statement: Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.
from datetime import datetime

class Product:

    def __init__(self):
        self.name = input("What's the product? : ")
        self.manufacturing_date = input("Enter mfg date(DD-MM-YYYY): ")
        self.expiry_date = input("Enter expiry date(DD-MM-YYYY): ")

        self.manufacturing_date = datetime.strptime(self.manufacturing_date, "%d-%m-%Y")
        self.expiry_date = datetime.strptime(self.expiry_date, "%d-%m-%Y")

    def expiry_left(self):

        today = datetime.today()
        # print(today)

        if self.expiry_date < today:
            print("The product has already expired.")

        else:
            diff = self.expiry_date - today
            days = diff.days

            years = days // 365
            days = days % 365
            months = days // 30
            days = days % 30

            print("Time left for expiry:")
            print("Years:", years)
            print("Months:", months)
            print("Days:", days)






p = Product()
p.expiry_left()
p.expiry_left()






    # def remaining_time(self):

    #     today = date.today()


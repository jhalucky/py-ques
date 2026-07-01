# Statement: Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.
from datetime import date

class Product:

    def __init__(self, name, manufacturing_date, expiry_date):
        self.name = name
        self.manufacturing_date = manufacturing_date
        self.expiry_date = expiry_date


    def remaining_time(self):

        today = date.today()

        
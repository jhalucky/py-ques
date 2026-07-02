class Scoop:
    total_scoops = 0

    def __init__(self, flavor):
        self.flavor = flavor
        self.__price = None
        Scoop.total_scoops += 1


    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    

    def __str__(self):
        return f"Flavor - {self.flavor}\nPrice - {self.get_price()}"
    
    @classmethod
    def sold(cls):
        print(f"{cls.total_scoops} scoops sold.")


class Bowl:

    total_bowls = 0
    
    def __init__(self):
        self.__scoop_list = []
        Bowl.total_bowls += 1


    def add_scoops(self, *scoops):
        for scoop in scoops:
            self.__scoop_list.append(scoop)


    def display(self):
        total = 0
        print("Displaying Bowl")
        for scoop in self.__scoop_list:
            print(f"Flavor - {scoop.flavor}\nPrice - {scoop.get_price()}")
            total += scoop.get_price()

        print(f"Price of Bowl: {total}")

    def __str__(self):
        return "\n".join(scoop.flavor for scoop in self.__scoop_list)
    
    @classmethod
    def sold(cls):
        print(f"{cls.total_bowls} bowls sold.")


choco = Scoop("Chocolate")
choco.set_price(120)
# print(choco)

berry = Scoop("Strawberry")
berry.set_price(100)
# print(berry)

vanilla = Scoop("Vanilla")
vanilla.set_price(100)

bowl = Bowl()

bowl.add_scoops(choco, berry, vanilla)
print(bowl)

bowl.display()
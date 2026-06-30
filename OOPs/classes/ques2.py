class BankAccount:

    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self,amount):
        deposit_amount = amount
        self.balance = self.balance + deposit_amount
        return self.balance

    def Withdrawal(self, amount):
        withdrawal_amount = amount
        self.balance = self.balance - withdrawal_amount
        return self.balance

    def bankFees(self, percentage):
        amount_percentage = 5/100 * self.balance
        return amount_percentage


    def display(self):
        return f"Account Number: {self.accountNumber}\nAccount Holder: {self.name}\nAccount Balance: {self.balance}"


newAccount = BankAccount(234567890,"Lucky Jha",5000)
newAccount.Deposit(1000)
newAccount.Withdrawal(3200)
print(newAccount.display())
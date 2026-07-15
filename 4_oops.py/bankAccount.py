class Account:
    def __init__(self,name, balance):
        self.balance=balance
        self.name=name
        print(f"Account Holder Name: {self.name}\n Balance: {self.balance}")

    def deposit(self, amount):
        self.balance+=amount
        print(f"New Balance is: {self.balance}\n")

    def withdraw(self,amount):
       
       if self.balance-amount < 0:
            print(f"Low Balance; {amount} cannot be withdrawn as current balance is {self.balance}\n")
       else:
            self.balance-=amount
            print(f"Amount {amount} withdrawn successfully; Remaining Balance: {self.balance}\n")
          
mohsin=Account("Mohsin Khan", 5000)
mohsin.deposit(2000)
mohsin.withdraw(3000)
mohsin.withdraw(5000)
mohsin.withdraw(3000)
mohsin.withdraw(5000)
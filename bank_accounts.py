class BalanceException(Exception):
    pass 

class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created. \nBalance = $ {self.balance:.2f}")
        
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance() # calls the  method within function
        
    def viableTransaction(self,amount): # checks if withdrawal can be done according to balance
        if self.balance >=amount:
            return
        else:
            raise BalanceException(f"\nAccount '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
    
    def transfer(self, amount, account):
        try:
            print('\n*******\n\nBeginning Transfer!')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! \n\n********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. {error}')
            
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05) #Additional interest
        print("\nDeposit complete.")
        self.getBalance()
            
            
class SavingsAcct(InterestRewardsAcct):
    def __init__(self,initialAmount, acctName):
        super().__init__(initialAmount,acctName)
        self.fee = 5
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
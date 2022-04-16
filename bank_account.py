
#Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber, name , balance.

class BankAccount():
    def __init__(self, account_number,balance,name):
        self.account_number= account_number
        self.name= name
        self.balance=balance
    
#Create a deposit() method which manages the deposit actions. (deposit() method will take parameter d and you will increase the balance with the amount d)

    def deposit(self,d):
        self.balance= self.balance + d

#Create a withdrawal() method which manages withdrawals actions. (withdrawal() method will take parameter w, you will reduce the amount of balance with w, if w is larger than the balance: then print Impossible operation! Insufficient balance!")

    def Withdrawal (self,w):
        if (self.balance< w):
          print("Impossible operation! Insufficient balance!")
        else:
          self.balance = self.balance - w
          
          
#Create a bankFees() method to apply the bank fees with a percentage of 5% of the balance account. (When this method is called, the balance amount should reduce 5%)

    def bankFees(self):
        
        
        
#Create a display() method to display account details.

     def display(self):
        print("Account Number : " , self.account_number)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
        
        
        
class BankAccount:
    def __init__(self,account_no,Balance):
        self.x=account_no
        self.y=Balance
    def deposite_amount(self):
        print("Enter the deposite amount")
        amount=int(input())
        print(f"your account is deposited with {amount}")
        self.k=self.y+amount
        print(f"Your available balance is{self.k}")
    def withdraw(self):
        print("Enter the amount to withdraw ")
        self.w_amount=int(input())
        print(f"Withdraw amount is {self.w_amount}")
        self.m=self.k-self.w_amount
        print(f"Your available balance is{self.m}")
    def Balance(self):
        print(f"Account number:{self.x}")
        print(f"Current available balance is{self.m}")
c1=BankAccount(3453,1000)
c1.deposite_amount()
c1.withdraw()
c1.Balance()

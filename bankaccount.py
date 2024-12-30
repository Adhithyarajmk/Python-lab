class Bankaccount:
    def __init__(self,accno,name,acctype,balance):
        self.account_no=accno
        self.name=name
        self.account_type=acctype
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited {amount}.new balance:{self.balance}")

    def withdraw(self,amount):
        if amount<=0:
            print("insufficient balance")
    def display_acc_info(self):
        print("Account number:",self.account_no)
        print("Account holder:",self.name)
        print("Account type:",self.account_type)
        print("Balance:",self.balance)
def display_menu():
    print("\n----- Bank Account Menu -----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Display Account Details")
    print("4. Exit")
    print("----------------------------")
def main():
    acc1= (100, "Ram", "savings", 1000)
while True:
     display_menu()
     choice= int(input("enter the choice:"))
     if choice==1:
          amount = float(input("Enter amount to deposit: $"))
          acc1.deposit(amount)
     elif choice == 2:  # Withdraw
           amount = float(input("Enter amount to withdraw: $"))
           acc1.withdraw(amount)

     elif choice == 3:
           acc1.display_acc_info()

     elif choice == 4:
         print("Thank you for using the Bank Account System!")
         break
     else:
      print("Invalid choice. Please try again.")

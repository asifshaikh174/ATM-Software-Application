import random

class ATM():
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: ", self.balance)
        print()

    def change_pin(self):
        old = int(input("Enter old pin: "))
        if old == self.pin:
            self.new = int(input("Enter new pin: "))
            self.pin = self.new
            print("Pin Changed Successfully!!!")
            print()

        else:
            print("Wrong Pin")
            print()
    def check_balance(self):
        print("Your Balance Is: ",self.balance)

    def withdraw(self,amount):
        self.amount= amount
        if self.amount > self.balance:
            print("InSufficient Fund!!!")
        else:
            self.balance = self.balance - self.amount
            print("Current account balance: ", self.balance)
            

    def account_detail(self):
        p=int(input("Enter Pin: "))
        if p == self.pin:
            print("\n----------ACCOUNT DETAIL----------")
            print(f"Account Holder: {self.name.upper()}")
            print(f"Account Number: {self.account_number}")
            print(f"Available balance: {self.balance}\n")
        else:
            print("Wrong Pin")


    def transaction(self):
        # print("\t\t1. Account detail\n\t\t2. Deposit Money\n\t\t3. Withdraw Money\n\t\t4. Check Balance\n\t\t5. Change Pin\n\t\t6.exit\n")

        while True:
            try: 
                option = int(input("\n\t1. Account detail\n\t2. Deposit Money\n\t3. Withdraw Money\n\t4. Check Balance\n\t5. Change Pin\n\t6.exit\n Enter a number to proceed: "))
            except:
                print("Enter Valid Details")
                continue
            else:
                if option == 1:

                    atm.account_detail()    
                elif option == 2:
                    amount = int(input("How much You Want to Deposit: "))
                    atm.deposit(amount)
                elif option == 3:
                    amount = int(input("How Much You Want To Withdraw: "))
                    atm.withdraw(amount)
                elif option == 4:
                    atm.check_balance()
                elif option == 5:
                    atm.change_pin()
                elif option==6:
                     print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: {self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                     exit()
                    

print("**********WELCOME TO BANK OF INDIA**********")
Name=input("Enter Your Name: ")
pin =int(input("Generate Pin: "))
Account_number = random.randint(10000000000,999999999999)
print("Your Account Number is: ",Account_number)
atm = ATM(Name, Account_number)

while True:
    trans = input("Do you want to Proceed?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")

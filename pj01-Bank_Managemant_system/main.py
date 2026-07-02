# Bank Management System
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'C:\\python-phase-3\\pj01-Bank_Managemant_system\\customer_data.json'  # main json file path
    data = []      # Dummy data
    try:
        if Path(database).exists():
            with open(database) as f:
                data = json.loads(f.read())
        else : 
            print("No such file exist..")

    except Exception as err:
        print(f"An error occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as f:
            f.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=4)
        num = random.choices(string.digits,k =4)
        spchar = random.choices("@#$%&*",k = 1)
        id = alpha+num+spchar
        random.shuffle(id)   #it return as object
        return "".join(id)   # I return it as a string.

    def createaccount(self):
            info = {
                "name" : input("Enter Your Name : "),
                "age"  : int(input("Enter your age : ")),
                "email" : input("Enter your Email : "),
                "phone" : int(input("Enter your Phone number : ")),
                "pin" : int(input("Enter your 4 digit pin : ")),
                "account_no." : Bank.__accountgenerate(),
                "balence" : 0
            }
            if info['age'] <12 or len(str(info['pin']))!= 4:
                print("You can't create your account..")
            else:
                print("Account created successfully...")
                for i in info:
                    print(f"{i} : {info[i]}")
                print("Please note your account number")
        
                Bank.data.append(info)
                Bank.__update()

    def depositmoney(self):
        account = input("Enter your account number : ")
        pin = int(input("Enter your pin number : "))

        userdata = [i for i in Bank.data if i['account_no.'] == account and i['pin'] == pin]

        if userdata == False:
            print("No such data found..")
        
        else:
            amount = int(input("Enter the amount you want to deposit : "))
            if amount > 10000 :
                print("Amount is too much you can deposit below 10k.")
            
            elif amount<100:
                print("You cant deposit below 100")

            else:
                userdata[0]['balence'] += amount
                Bank.__update()
                print("Amount deposited Successfully.")

    def withdrawmoney(self):
        account = input("Enter your account number : ")
        pin = int(input("Enter your pin number : "))

        userdata = [i for i in Bank.data if i['account_no.'] == account and i['pin'] == pin]

        if not userdata:
            print("No such data exist.")
        
        else:
            amount = int(input("Enter your withdraw amount : "))
            if amount > userdata[0]['balence']:
                print("You dant have sufficient money.")

            elif amount <100:
                print("You can't withdraw below 100")
            
            else:
                userdata[0]['balence'] -= amount
                Bank.__update()
                print("Ammount withdrew successfully.")


user = Bank()

print("Press 1 for Creating Account. ")
print("Press 2 for Depositing Money. ")
print("Press 3 for Withdrawing Money. ")
print("Press 4 for Account Details. ")
print("Press 5 for Updatng Details. ")
print("Press 6 for Deleting your Account. ")

check = int(input("Tell your responce : "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()
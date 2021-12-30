class Atm:
    def __init__(self,cardnumber,pin) :
        self.cardnumber=cardnumber
        self.pin=pin

    def checkbalance(self):
        print("your balance is 50000")

    def withdrawl(self,amount):
        newamount=50000-amount

        print("your withdrawl amount is "+str(amount)+" your remaining balance is "+str(newamount))

def main() :
    cardno=input("enter your card number ")
    pinno=input("enter your pin number ")

    newuser= Atm(cardno,pinno)
    print("choose your activity 1. balance enquiry 2. withdrawl")
    activity=int(input("enter activity number "))
    if(activity==1):
        newuser.checkbalance()

    elif(activity==2):
        amount=int(input("enter the amount "))
        newuser.withdrawl(amount)
    else:
        print("enter a valid number")
main()


        

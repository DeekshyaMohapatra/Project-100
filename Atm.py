class Atm:
    def __init__(self,atmcardnumber,pincode):
        self.atmcarnumber = atmcardnumber
        self.pincode = pincode
    
    def checkbalance(self):
        print("Your balance is 10000")

    def withdrawl(self,amount):
        newamount = 10000 - amount
        print("You have withdrawn"+str(amount) +". Your remaining balance is "+ str(newamount))


def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin code:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.checkbalance()
    elif (activity == 2):
        amount = int(input("Enter the amount you want to withdraw:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()


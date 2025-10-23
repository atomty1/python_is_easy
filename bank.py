print("Welcome to Taye's bank")
balance = float(input("Enter the amount you want to deposit: "))
def bank():
    print("What do you want to do?")
    menu = input("1. Add more money 2. Withdraw 3. Check balance: ")
    if(menu == "1"):
        add_money()
    elif(menu == "2"):
        withdraw_money()
    elif(menu == "3"):
        display_balance()
    else:
        print("Invalid input")
    
    repeat = input("Do you want to do anything else? 1. Yes 2. No")
    if(repeat == "1"):
        bank()
    else:
        print("Thanks for coming")

def add_money():
    global balance
    amount = float(input("Enter amount you want to add: "))
    balance = balance + amount
    print("Money added successfully")

def withdraw_money():
    global balance
    amount = float(input("Enter amount you want to withdraw: "))
    if(amount <= balance):
        balance = balance - amount
        print("Money withrawn successfully")
    else:
        print("Insufficient funds")

def display_balance():
    print("You have ", balance)

bank()
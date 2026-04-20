class InsufficientBalance(Exception):
    pass

balance = 0

def deposit(amount):
    global balance
    if amount < 0:
        raise ValueError("Invalid Amount")
    else:
        balance += amount
        print("Deposited Successfully!")
        print("Total balance is :",balance)

def withdraw(amount):
    global balance
    if amount > balance:
        raise InsufficientBalance("Not enough funds, Your balance is", balance)
    else:
        balance-=amount
        print("Withdrawal Successful")
        print("Current balance is:",balance)

deposit(34)
deposit(100)
withdraw(50)
withdraw(100)

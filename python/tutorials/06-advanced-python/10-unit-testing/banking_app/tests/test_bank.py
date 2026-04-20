import pytest
from src.bank import BankAccount

def test_create_account():
    account = BankAccount("Lata Patel",5000)
    assert account.owner == "Lata Patel"
    assert account.balance == 5000

def test_deposit():
    account = BankAccount("Lata Patel",100)
    account.deposit(40)
    account.deposit(50)
    assert account.balance == 190

    with pytest.raises(ValueError):
        account.deposit(-40)

def test_withdraw():
    account = BankAccount("Satya Jit",200)
    account.withdraw(50)
    account.withdraw(100)
    assert account.balance == 50

    with pytest.raises(ValueError):
        account.withdraw(300)

def test_get_balance():
    account  = BankAccount("Imran",200)
    assert account.get_balance() == 200
import pytest
from customers_db import CustomersDB

def test_insert_customer():
    db = CustomersDB()
    db.connect()

    db.insert_customer("Alex","alex34@gmail.com")
    customer = db.get_customer_by_name("Alex")
    assert customer is not None
    assert customer['name'] == "Alex"
    assert customer['email'] == "alex34@gmail.com"

    db.clear_customer()
    db.close()


def test_get_all_customers():
    db = CustomersDB()
    db.connect()

    db.insert_customer("Ansh", "ansh34@gmail.com")
    db.insert_customer("Khushi","khushi23@gmail.com")

    customers = db.get_all_customers()
    assert len(customers) == 2

    db.clear_customer()
    db.close()

import pytest
from customers_db import CustomersDB

@pytest.fixture()
def db():
    db_instance = CustomersDB()
    db_instance.connect()
    yield db_instance
    db_instance.clear_customer()
    db_instance.close()

def test_insert_customer(db):

    db.insert_customer("Alex","alex34@gmail.com")
    customer = db.get_customer_by_name("Alex")
    assert customer is not None
    assert customer['name'] == "Alex"
    assert customer['email'] == "alex34@gmail.com"


def test_get_all_customers(db):

    db.insert_customer("Alex", "alex34@gmail.com")
    db.insert_customer("Khushi","Khushi23@gmail.com")

    customers = db.get_all_customers()
    assert len(customers) == 2

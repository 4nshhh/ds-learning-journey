import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        database = "expense_manager"
    )

    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Failed to connect")

    cursor = connection.cursor(dictionary= True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",(expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit = True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES(%s,%s,%s,%s)",
            (expense_date, amount, category, notes)
        )


def delete_expense_for_date(expense_date):
    with get_db_cursor(commit= True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


if __name__ == "__main__":
    fetch_all_records()
    # fetch_expenses_for_date("2024-08-02")
    # insert_expense("2024-09-02",1000,"Food","Pizza")
    # delete_expense_for_date("2024-09-02")


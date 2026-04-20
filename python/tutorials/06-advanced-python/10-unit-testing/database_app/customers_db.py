class CustomersDB:
    def __init__(self):
        self.customers = []
        self.next_id = 1
        self.connection = None

    def connect(self):
        self.connection = "DummyConnectionObject"
        print("Connected to the Database")

    def insert_customer(self,name,email):
        customer = {
            "id" : self.next_id,
            "name" : name,
            "email" : email
        }
        self.customers.append(customer)
        self.next_id += 1

    def get_all_customers(self):
        return self.customers

    def get_customer_by_name(self, name):
        for customer in self.customers:
            if customer["name"] == name:
                return customer
        return None

    def clear_customer(self):
        self.customers = []
        self.next_id = 1

    def close(self):
        self.connection = None
        print("Database Connection Closed")

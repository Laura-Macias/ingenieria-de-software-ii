from .user import User

class Customer (User) :

    def __init__(self, id_customer, name_customer, last_name_customer, address_customer, phone_customer, email_customer):
        super().__init__(name_customer, last_name_customer, address_customer, phone_customer, email_customer)
        self.id_customer = id_customer
    
    def get_id(self):
        return str(self.id_customer)
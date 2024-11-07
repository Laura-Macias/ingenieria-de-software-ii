from .user import User

class Customer (User) :

    def __init__(self, id_costumer, name, last_name, address, phone, email):
        super().__init__(name, last_name, address, phone, email)
        self.id_costumer = id_costumer
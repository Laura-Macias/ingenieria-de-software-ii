from flask_login import UserMixin


# Definir la clase User que hereda de UserMixin para compatibilidad con Flask-Login
class User(UserMixin):

    def __init__(self, id_customer, name, last_name, address, phone, email):
        self.id = id_customer 
        self.name = name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
from flask_login import UserMixin

# Definir la clase User que hereda de UserMixin para compatibilidad con Flask-Login
class User(UserMixin):
    def __init__(self, id_customer, name, email):
        self.id = id_customer 
        self.name = name
        self.email = email
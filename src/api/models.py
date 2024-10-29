from flask_login import UserMixin
from config import Config


# Definir la clase User que hereda de UserMixin para compatibilidad con Flask-Login
class User(UserMixin):

    def __init__(self, id_customer, name, email):
        self.id = id_customer 
        self.name = name
        self.email = email

class Catalogo :

    def __init__(self, id_catalog, product_name, description, price, stock, update_date):

      self.id_catalog = id_catalog
      self.product_name = product_name
      self.description = description
      self.price = price
      self.stock = stock
      self.update_date = update_date

    
    def serialize(self):
        return {
            'id_catalog': self.id_catalog,
            'product_name': self.product_name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'update_date': self.update_date
        }




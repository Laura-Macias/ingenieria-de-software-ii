class Catalogo :

    def __init__(self, id_catalog, product_name, description, price, stock, update_date, image):

      self.id_catalog = id_catalog
      self.product_name = product_name
      self.description = description
      self.price = price
      self.stock = stock
      self.update_date = update_date
      self.image = image

    
    def serialize(self):
        return {
            'id_catalog': self.id_catalog,
            'product_name': self.product_name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'update_date': self.update_date,
            'image': self.image
        }
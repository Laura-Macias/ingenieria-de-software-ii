class Catalogo :

    def __init__(self, id_catalog, service_name, description, price, availability, update_date, image):

      self.id_catalog = id_catalog
      self.service_name = service_name
      self.description = description
      self.price = price
      self.availability = availability
      self.update_date = update_date
      self.image = image

    
    def serialize(self):
        return {
            'id_catalog': self.id_catalog,
            'product_name': self.service_name,
            'description': self.description,
            'price': self.price,
            'availability': self.availability,
            'update_date': self.update_date,
            'image': self.image
        }
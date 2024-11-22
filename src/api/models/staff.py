from .user import User

class Staff (User) :

    def __init__(self, id_staff, name_staff, last_name_staff, position_staff, address_staff, phone_staff, email_staff):
        super().__init__(name_staff, last_name_staff, address_staff, phone_staff, email_staff)
        self.id_staff = id_staff
        self.post = position_staff

    def __repr__(self):
        return (f"Staff(id_staff={self.id_staff}, name_staff={self.name}, "
                f"last_name_staff={self.last_name}, position_staff={self.post}, "
                f"address_staff={self.address}, phone_staff={self.phone}, email_staff={self.email})")
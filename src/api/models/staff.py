from .user import User

class Staff (User) :

    def __init__(self, id_staff, name_staff, last_name_staff, position_staff, address_staff, phone_staff, email_staff):
        super().__init__(name_staff, last_name_staff, address_staff, phone_staff, email_staff)
        self.id_staff = id_staff
        self.post = position_staff
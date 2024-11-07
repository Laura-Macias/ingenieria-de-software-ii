from .user import User

class Staff (User) :

    def __init__(self, id_staff, name, last_name, post, hire_date, salary, address, phone, email):
        super().__init__(name, last_name, address, phone, email)
        self.id_staff = id_staff
        self.post = post
        self.hire_date = hire_date
        self.salary = salary
class User:
    def __init__(self, first_name, middle_name, last_name, email, password, role=0):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role
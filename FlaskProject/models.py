class User:
    def __init__(self, first_name, middle_name, last_name, email, password, role=0):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role

class UserView:
    def __init__(self, id, first_name, middle_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email      

class Booking:
    def __init__(self, id, email, place, bookingDate, remarks):
        self.id = id
        self.email = email
        self.place = place
        self.bookingDate = bookingDate
        self.remarks = remarks
       
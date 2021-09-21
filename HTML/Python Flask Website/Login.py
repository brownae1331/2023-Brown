import re
class Users():

    def __init__(self, email, password, fname, lname):
        self.email = email
        self.password = password
        self.first_name = fname
        self.last_name = lname

    def check_password(self):
        if (any(x.isupper() for x in self.password) and len(self.password) >= 6 and len(self.password) <= 12):
            return True
        else:
            return False
    
    def check_email(self):
        email_format = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if email_format.match(self.email):
            return True
        else:
            return False
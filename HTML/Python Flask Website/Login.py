class Users():
    def __init__(self, email, password, fname, lname):
        self.email = email
        self.password = password
        self.first_name = fname
        self.last_name = lname

    def check_password(self):
        if (any(x.isupper() for x in self.password)):
            print("correct")

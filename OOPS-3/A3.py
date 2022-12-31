# Returning Classs Variable
class students:
    krishna='Vasudev' # Class Variable
    def __init__(self) : # Instance Method
        self.marks=66 # Instance Variable

    def get_darks(self):
        return self.marks
    # -------------------

    def god(cls): # CLS stands for Class
        return cls.krishna
    # --------------------
s1=students()

print(s1.god())
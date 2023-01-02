# Method Overriding

class father:
    def phone(self):
        print("NOKIA")
class child(father):
    def phone(self):
        print("ASUS")

obj=child()
obj.phone()
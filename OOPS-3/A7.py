# Single-Level Inheritance 

class abc:
    def show(self):
        print("This is 'SHOW' belong's to 'ABC'")

class xyz(abc): # Above Class Name is in the Brackets
    def hide(self):
        print("This is 'HIDE' belong's to 'XYZ'")

q1=xyz() # Object of xyz
q1.show() # Method of ABC Class
q1.hide()

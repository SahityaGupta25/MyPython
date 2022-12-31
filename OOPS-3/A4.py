# Returning Class Variable 2
class students:
    krishna='Vasudev'
    def __init__(self) :
        self.marks=66
    
    # By After Writting this class method my compiler knows that this is a CLASS METHOD
    @ classmethod 
    def god(self): 
        return students.krishna
        # This is Class Method as you can see it is dealing with Class Variable.

q1=students()

print(students.god())
   
        

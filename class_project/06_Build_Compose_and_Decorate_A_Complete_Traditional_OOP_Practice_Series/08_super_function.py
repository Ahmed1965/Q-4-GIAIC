# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    def __init__(self,name, subject):
        super().__init__(name) # Call the constructor of the base class
        self.subject = subject
        
    def display(self):
        print(f'Name: {self.name}')
        print(f'Subject: {self.subject}')
        
person = Person('Anas Seth')

teacher = Teacher('Anas Seth', 'Python')
print(f'The Teacher Name is {person.name} and he teaches us {teacher.subject}')
# teacher.display()        

    
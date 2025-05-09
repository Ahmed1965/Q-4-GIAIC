# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


# Creating Class Employee
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # public variable
        self._salary = salary # protected variable
        self.__ssn = ssn # private variable
        
        
    def display(self):
        print(f'Name: {self.name}')
        print(f'Name: {self._salary}')
        print(f'Name: {self.__ssn}')
        
# creating an object of Employee class        
if __name__ == '__main__':
    emp = Employee('Arshad',1000, 123456789)
    emp.display()
    print(emp.name) # Accessing public variable 
    print(emp._salary) # Accessing protected variable (not recommended)
    print(emp.get_ssn()) # Accessing private variable (will raise an AttributeError)  
    
    
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        
    def display_info(self):
        print(f"The Employee ID is : {self.emp_id}")
        print(f"The name of Employee is : {self.name} ")
        print(f"The position of Employee is : {self.position} ")
    

class Department:
    def __init__ (self, employee, name):
        self.employee = employee  # aggregation has an object of employee
        self.name = name
        
    def display_department_info(self):
        print(f"Department Name : {self.name}")
        print("Employee Detail : ")
        self.employee.display_info()
        
# create an employee object

employee = Employee(101, "Ejaz", "Manager") 
# pass employee in department (aggregation)
department = Department(employee, "Management" )

department.display_department_info()


    


    
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Students:
    
    def __init__(self, name, grade):
        
        self.name = name
        self.grade = grade
        
    def display(self):
        print(f'The student {self.name} acquired grade {self.grade}')
        
my_name_dict : dict = {'Rafiq': 'A', 'Waheed':'B', 'Moeez':'C'}
        
for name,grade in my_name_dict.items():
        student = Students(name,grade)
        student.display()
    
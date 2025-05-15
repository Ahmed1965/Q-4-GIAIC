# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
age:int = 0

def check_age():
    try:
        if age < 18:
            raise Exception("Invalid age error")
        else:
            print('Age is valid')
    
    except Exception as e:
        return str(e)       
print(check_age())
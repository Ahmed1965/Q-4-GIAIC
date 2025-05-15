# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

class ClassDecorator:
    def __init__(self, cls):
        self.cls = cls
        
    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)

def greet(add_greeting):
    print("Hello from decorators")
    
@ClassDecorator
class Person:
    def __init__(self, name):
        self.name = name
        print("Greeting")

j = Person("Alice")

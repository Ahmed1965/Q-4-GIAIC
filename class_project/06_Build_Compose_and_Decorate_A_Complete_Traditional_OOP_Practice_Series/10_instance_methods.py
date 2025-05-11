# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof! I am a {self.breed}.")
# Create an instance of the Dog class and call the bark() method
dog1 = Dog("Buddy", "Golden Retriever") 
dog1.bark()  # Output: Buddy says Woof! I am a Golden Retriever.
# Create another instance of the Dog class and call the bark() method   
dog2 = Dog("Max", "Bulldog")
dog2.bark()  # Output: Max says Woof! I am a Bulldog.

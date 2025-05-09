# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self, name):
        """Constructor object is created"""
        self.name = name
        print(f'Object {self.name} created ')
    def __del__(self):  
        """Destructor object is destroyed"""
        print(f'Object {self.name} destroyed')
if __name__ == '__main__':
    logger1 = Logger('Logger1')
    logger2 = Logger('Logger2')
    del logger1  # Explicitly deleting the object to trigger the destructor
    del logger2  # Explicitly deleting the object to trigger the destructor
        

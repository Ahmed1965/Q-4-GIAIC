# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        
    def start(self):
        return f"Engine with {self.horsepower} started"
    
    def stop(self):
        return f"The engine with {self.horsepower} is stopped"
    
    def __str__(self):
        return f"Engine (Horsepower: {self.horsepower})"
    
class Car:
    def __init__(self, brand, model, engine ):
        self.brand = brand
        self.model = model
        self.engine = engine  # composition Car has-a relation with engine
        
    def car_start(self):
        return f"{self.brand} with {self.model}: {self.engine.start()}"
    
    def car_stopped(self):
        return f"{self.brand} with {self.model}: {self.engine.stop()}"
    
    def __str__(self):
        return f"{self.brand} {self.model} with {self.engine}"

# Create an engine instance
engine = Engine(200)

# Create a car with the engine instance
car = Car("Halval", "E6", engine)

# Print the objects
print(engine)
print(car)

# Demonstrate the composition by using car methods
print(car.car_start())
print(car.car_stopped())
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b
    
a,b = 5, 10
result = MathUtils.add(a,b)
print(f"The sum of {a} and {b} is: {result}")  
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    
    count = 0  # Class variable to keep track of the number of instances

    def __init__(self):
        Counter.count += 1  # Increment the count whenever a new instance is created

    @classmethod
    def get_count(cls):
        """Class method to return the current count of instances."""
        return cls.count
Counter1 = Counter()
Counter2 = Counter()        
Counter3 = Counter()        
Counter4 = Counter()        

print(f"Number of Counter instances created: {Counter.get_count()}")  # Output: Number of Counter instances created: 

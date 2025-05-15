# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

class LogFunctionCall:
    def __init__(self,func):
        self.func = func
        
    def __call__(self, *args, **kwargs ):
        print('Function is being Called')
        return self.func(*args, **kwargs)
    
@LogFunctionCall

def say_hello():
    print("Hello")

say_hello()        
        

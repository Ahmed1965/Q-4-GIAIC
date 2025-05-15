# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.


# Creating class A

class A:
    def show(self):
        print("This is A's show()")
        
# subclass B inherits from A
        
class B(A):
    def show(self):
        print("This is B's show()")
        
# subclass C inherits from A 
        
class C(A):
    def show(self):
        print("This is C's show()")
        
class D(B,C):
    def show(self):
        print("This is D's in B Show()")
        
class D(C):
    pass  # Inherits show() from B (because B is before C in the MRO
        
a = A()

b = B()

c = C()



a.show()
b.show()
c.show()
d.show()
        
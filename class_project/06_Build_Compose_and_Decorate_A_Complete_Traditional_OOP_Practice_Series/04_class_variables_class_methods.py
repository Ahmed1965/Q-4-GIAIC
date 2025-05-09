# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = 'Default Bank'
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
print(f"Initial Bank Name: {Bank.bank_name}")  # Output: Initial Bank Name: Default Bank
Bank.change_bank_name('UBL Bank')
print(f"Updated Bank Name: {Bank.bank_name}")  # Output: Updated Bank Name: UBL Bank
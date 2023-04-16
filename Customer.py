#Customer.py
# The Person class holds the following data about a person with data attributes
#name, address, and mobile number

class Person:
    # The __init__ method initializes data attributes for Name, Address, and
    #Mobile number

    def __init__(self, name, address, mobile_number):
        self.name = name
        self.address = address
        self.mobile_number = mobile_number

    # Defining the mutators for the class's data attributes

    def set_name(self, name):
        self.name = name
    def set_address(self, address):
        self.address = address
    def set_mobile_number(self, mobile_number):
        self.mobile_number = mobile_number

    # Defining the accessors for the class's data attributes

    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_mobile_number(self):
        return self.mobile_number

# Create a subclass named Customer with data attributes for a customer ID,
# and a Boolean data attribute iindicating whether the customer
# wishes to be on a mailing list.

class Customer(Person):
    
    # The init method accepts arguments for the name, address, mobile number
    # customer ID, and Boolean data attribute asking "Yes or No" to whether
    # the customer wishes to be on a mailing list.

    def __init__(self, name, address, mobile_number, customer_id, mailing_list):
        # call the superclass __init__ method
        Person.__init__(self, name, address, mobile_number)
        

    # Initialize the customer ID and mailing list attribute
        self.customer_id = customer_id
        self.mailing_list = mailing_list

    # Defining the mutators

        def set_customer_id(self, customer_id):
            self.customer_id = customer_id
        def set_mailing_list(self, mailing_list):
            self.mailing_list = mailing_list

    # Defining the accessors

        def get_customer_id(self):
            return self.customer_id
        def get_mailing_list(self):
            return self.mailing_list

# Define the main function
def main():
    

    name = input("Enter the name: ")
    address = input("Enter the address: ")
    mobile_number = input("Enter the mobile number: ")
    customer_id = input("Enter the customer ID: ")
    mailing_list = input("Does the customer wish to be on the mailing list?(Yes/No): ")

    if mailing_list == 'Yes':
        mailing_list = True
    
    else:
        mailing_list = False
    
    customer = Customer(name, address, mobile_number, customer_id, mailing_list)

# Display the results
    print("\nCustomer information:")
    print("Name:", customer.name)
    print("Address:", customer.address)
    print("Mobile Number:", customer.mobile_number)
    print("Customer ID:", customer.customer_id)
    print("On Mailing List:", customer.mailing_list)

# Calling the main function
main()
    

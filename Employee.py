#Employee.py

#The Employee class holds the following data about an employee
#with attributes: Name, ID, Department and Title.

class Employee:

    #the __init__ method initializes data attributes for Name, ID, Department,
    #and Title

    def __init__(self, name, id, department, title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title

    #defining the mutators for the class's data attributes

    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_department(self, department):
        self.__department = department
    def set_title(self, title):
        self.__title = title

    #defining the accessors for the class's data attributes

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_department(self):
        return self.__department
    def get_title(self):
        return self.__title

    #the results
    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"ID: {self.__id}")
        print(f"Department: {self.__department}")
        print(f"Title: {self.__title}")

#Define main function
def main():
    #Create three objects from Employee class
    employee_1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee_2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee_3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    #Display the employees' information
    print("Employee 1: ")
    employee_1.display_info()
    print()

    print("Employee 2: ")
    employee_2.display_info()
    print()

    print("Employee 3: ")
    employee_3.display_info()

#Call the main function
main()
    

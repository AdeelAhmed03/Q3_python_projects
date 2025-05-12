class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Ali", 5000, "123-45-6789")

print("Name: ", emp.name)

print("Salary: ", emp._salary)

try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable: ", e)

print("Accessing private variable with name mangling:", emp._Employee__ssn)


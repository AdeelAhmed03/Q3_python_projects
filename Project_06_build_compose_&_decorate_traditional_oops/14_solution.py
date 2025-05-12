class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def show_department_info(self):
        return f"Department: {self.department_name}, {self.employee.get_details()}"
    

emp = Employee("Adeel")

dept = Department("HR", emp)

print(dept.show_department_info())
class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return (self.name, self.marks)


student1 = Student("Adeel", 75)

print(student1.display())

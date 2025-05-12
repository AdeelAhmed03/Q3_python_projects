class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject_field):
        super().__init__(name)
        self.subject_field = subject_field

    def display_info(self):
        print(f"Name: {self.name}, Subject: {self.subject_field}")

t1 = Teacher("Hamzah Syed", "Python")
t1.display_info()
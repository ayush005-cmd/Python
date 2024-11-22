class person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def display(self):
        return f"Name: (self.name), Age: (self.age)"
class student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        return f"{super().display()},student ID:(self.student_id)"
        
class Teacher(person):
    def __init__(self,name,age,employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        return f"{super().display()},Employee ID: (self.employee_id)"

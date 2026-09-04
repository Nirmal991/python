class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')

    def print(self):
        print(f'Name          : {self.name}')
        print(f'City          : {self.city}')

class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.department = kwargs.get('department')
        self.salary = kwargs.get('salary')

    def print(self):
         print("========== EMPLOYEE ==========")
         super().print()
         print(f'Department    : {self.department}')
         print(f'Salary        : {self.salary}')

p1 = Person(name = "Nirmal",city = "Bengaluru")
# print(dir(p1))
p1.print()


e1 = Employee(name='Suresh', city='Jaipur', department='ADMIN', salary=55000)

print(e1.__dict__)

e1.print()

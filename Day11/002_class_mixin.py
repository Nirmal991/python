
class StateMixin:
    def Show_state(self):
        print("VARS: ", vars(self))
        print("DIR: ", dir(self))
        members = {mem:getattr(self,mem) for mem in vars(self)}
        print(members)

class Person:
    def __init__(self):
        self.id = 101
        self.name = "Sachin"
        self.age = 41
        
class Employee: 
    def __init__(self):
        self.eid = 102
        self.e_name = "tendulkar"
        self.salary = 100
        
class Product:
    def __init__(self):
        self.p_pid  = 111
        self.p_name = "nail polish"
        self.price = 125
        
class PersonIntrospect(Person, StateMixin):
    pass

class EmployeeIntrospect(Employee, StateMixin):
    pass

class ProductIntrospect(Product, StateMixin):
    pass


person_intro = PersonIntrospect()
employee_intro = EmployeeIntrospect()
product_intro = ProductIntrospect()
person_intro.Show_state()
employee_intro.Show_state()
product_intro.Show_state()
        
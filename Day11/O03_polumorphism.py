from abc import ABC,abstractmethod

class Account(ABC):
    @abstractmethod
    def do_job(self):
        pass
    
def Business(acc_lst):
    print("Business Started")
    for acc in acc_lst:
        acc.do_job()
    else:
        print("Completed All account type verification")
    print("Business Completed")
# print("_" * 60)
    
class Savings(Account):
    def do_job(self):
        print("Savings job done...")
        
class Current(Account):
    def do_job(self):
        print("Current job done")
        
class DMat(Account):
    def do_job(self):
        print("DMat job done")
        
class OD(Account):
    def do_job(self):
        print("OD job done")
        
# acc = Account()

sa = Savings()
print("SA", type(sa))
curr =  Current()
print("CURR", type(curr))
dmat = DMat()
print("DMAT", type(dmat))
list_obj = [sa, curr, dmat]
print(type(list_obj))
# Business(list_obj)

# sub_classes = [sub for sub in Account.__subclasses__()] # tell the subclass in it
sub_classes = [sub.__name__ for sub in Account.__subclasses__()]
print(sub_classes)
str_class_name = "Savings"
print(type(str_class_name))
sub_object =eval(f"{str_class_name}()")
# sub_object = [eval(f"{sub.__name__}()") for sub in Account.__subclasses__()]
print(type(sub_object))
# Business(sub_object)
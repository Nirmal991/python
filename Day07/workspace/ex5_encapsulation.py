class InvalidMarksException(Exception): pass

class Student:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__subject = kwargs.get('subject')
        self.__marks = kwargs.get('marks')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_marks(self, marks):
        if type(marks) not in (int, float):
            raise InvalidMarksException('Marks must be a number')

        if marks < 0 or marks > 100:
            raise InvalidMarksException('MArks must be between 0 and 100')

        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f'Student(name={self.__name!r}, subject={self.__subject!r}, marks={self.__marks!r})'

def main():
    pass
s1 = Student(name = "Nirmal", subject = "Phusics", marks = 99)
print(s1)
s2 = Student()
s2.set_name("suhani")
s2.set_marks(50)
print(s2)


main()
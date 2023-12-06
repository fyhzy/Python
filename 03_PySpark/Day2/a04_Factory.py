"""
    工厂模式
"""


class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        elif p_type == 't':
            return Teacher()


pf = PersonFactory()
worker = pf.get_person('w')
stu = pf.get_person('s')
tea = pf.get_person('t')

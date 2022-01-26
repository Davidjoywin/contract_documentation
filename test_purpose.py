from re import S


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self, nm):
        self.nm = nm
        return self.nm

    def get_age(self, age):
        self.ages = age
        return self.age

class Student(Person):
    pass


student = Student(45, 2020)
student.get_name("david")
student.get_age(50)
print(student.nm, student.ages)
from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Student(Person):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def eat(self):
        return "All food"

    def speak(self):
        return "English"

    def sleep(self):
        return "10 hours"
s1 = Student("John", 18, 'Student')
print(s1.eat())
print(s1.name)

class Univer(ABC):

    @abstractmethod
    def fak(self):
        pass

    @abstractmethod
    def talaba_num(self):
        pass
        pass

    @abstractmethod
    def proff(self):
        pass

class TUIT(Univer):
    def __init__(self, name, year, teacher_num):
        self.name = name
        self.year = year
        self.teacher_num = teacher_num

    def fak(self):
        return "AKT, KIF, DIF, TELKOM"

    def talaba_num(self):
        return "12 000"

    def proff(self):
        return "IT texnologiya"

t = TUIT("Tashkent Universitiy Information Texnology", 1955, 300)
print(t.fak())
print(t.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):

    def __init__(self, name, age, salary, work_place):
        Person.__init__(self, name, age)
        self.salary = salary
        self.work_place = work_place


class Student(Person):

    def __init__(self, name, age, univer_s, fak):
        super().__init__(name, age)
        self.univer_s = univer_s
        self.fak = fak



class PartTimeStudent(Employee, Student):
    def __init__(self, name, age, salary, work_place, univer_s, fak,  work_time, study_time):
        Employee.__init__(self, name, age, salary, work_place)
        Student.__init__(self, name, age, univer_s, fak)
        self.work_time = work_time
        self.study_time = study_time

    def get_info(self):
        return self.salary, self.fak, self.work_time

p1 = PartTimeStudent("Jackee", "18", "400$", "bank", "rty", "AKT", "9 hours", "twice a year")
print(p1.get_info())



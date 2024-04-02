class Car:
    def __init__(self, name,  mator, year, make,):
        self.__name = name
        self.mator = mator
        self.year = year
        self.make = make

    def get_Car_info(self):
        return self.__name, self.year
bmw = Car("BMW X7", "5.6", "2021", "BMW")
print(bmw.get_Car_info())


class Sport_car(Car):
    def __init__(self,name,  mator, year, make, type, speed,type_petrol ):
        Car.__init__(name,  mator, year, make)
        self.type = type
        self.speed = speed
        self.type_petrol = type_petrol
    def get_Sport_car_info(self):
        return self.type, self.speed, self.type_petrol
Sc = Sport_car("Stg","2.3", "2023", "BMW", "sport_car", "200 m/h", "gybrid")
print(Sc.get_Sport_car_info())
print(Sc.get_Car_info())

# class Person:
#     def __init__(self, name, age, surname, city):
#         self.name = name
#         self.age = age
#         self.surname = surname
#         self.city = city
#
#     def info_person(self):
#         return f"{self.name}\n{self.surname}\n{self.age}\n{self.city}"
#
#     def get_year(self):
#         import datetime
#         today = datetime.date.today()
#         year = today.year
#         return year-int(self.age)
#
#
# class Student(Person):
#     def __init__(self, name, age, surname, city, university, course, prof):
#         super().__init__(name, age, surname, city)
#         self.university = university
#         self.course = course
#         self.prof = prof
#
#     def get_univer_info(self):
#         return self.university, self.course, self.prof
#
# s1 = Student('Jahongir', 19, 'Qodirov', 'Surxandaryo', 'TATU', 1, 'AKT')
#
# print(s1.get_univer_info())
# print(s1.get_year())
# print(s1.info_person())

# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# # P1 = Person("Jahongir", "18", "2005")
#
# class Company:
#
#     def __init__(self, name_c, year, prof):
#         self.name_c = name_c
#         self.year = year
#         self.prof = prof
# # C1 = Company("EPAM", "2014", "IT")
#
# class Dev(Person, Company):
#     def __init__(self,name, age, gender, name_c, year, prof, level, prof_dev ):
#         Person.__init__(self,name, age, gender )
#         Company.__init__(self, name_c, year, prof)
#         self.level = level
#         self.prof_dev = prof_dev
#     def get_info(self):
#         return self.name, self.age, self.level
# D1 = Dev("Jahongir", "18", "Male", "EPAM", "2014", "IT", "Junior", "Backend")
# print(D1.get_info())


# class Univer:
#     def __init__(self, name_u, year, prof_u):
#         self.name_u = name_u
#         self.year = year
#         self.prof_u = prof_u
#     def get_univer_info(self):
#         return self.name_u, self.year, self.prof_u
#
# class Fakultet(Univer):
#     def __init__(self,name_u, year, prof_u, name_f, kafedra_soni):
#         Univer.__init__(self,name_u, year, prof_u)
#         self.name_f = name_f
#         self.kafedra_soni = kafedra_soni
#     def get_fakultet_info(self):
#         return self.name_f, self.kafedra_soni
#
# class Group(Fakultet):
#     def __init__(self,name_u, year, prof_u,name_f, kafedra_soni, group_num, Tuthor, stud_num):
#         Fakultet.__init__(self,name_u, year, prof_u,name_f, kafedra_soni)
#         self.group_num = group_num
#         self.Tuthor = Tuthor
#         self.stud_num = stud_num
#     def get_group(self):
#         return self.name_u, self.name_f, self.stud_num
# g1 = Group("TUIT", "1987", "Axborot Tex", "AKT", "5", "120-23", "Islom", "29")
#
# class Sudent
# class Sudent
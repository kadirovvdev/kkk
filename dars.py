
# 1
# from faker import Faker
# h = Faker()
# import random
#
#
# with open("test1.txt", "w") as file:
#     for i in range(1,11):
#         file.write(f"{i}  {h.name()}  {random.randint(1,100)}\n")
#
# with open('test1.txt', 'r') as file:
#     lines = file.readlines()
#     sorted_lines = sorted(lines, key = lambda x: int(x.split()[2]))
#
# with open("test2.txt", "w") as f:
#
#     for line in sorted_lines:
#
#         f.write(line)



# 2
#
# with open('test.txt', 'r') as file, open('output.txt', 'w') as out:
#
#
#     for i in file:
#         words = i.split()
#         for word in words:
#             if word[0].isupper():
#                 out.write(word + ' ')
#         out.write('\n')

# 3
# with open('test.txt', 'r') as file:
#
#
#     for i in file:
#         words = i.split()
#         s = 0
#         for word in words:
#             if len(word) < 5:
#                 s += 1
# print(s)

# 4
# with open('test.txt', 'r') as file:
#     count = 0
#     for line in file:
#         if not line.startswith('T'):
#             count += 1
# print(count)

"Finish"

# def say_hello(name, city, state):
#     a = ' '.join(name)
#     return (f"Hello, {a}! Welcome to {city}, {state}")




# k = int(input("Takrorlanishlar soni:"))
# for i in range(k):
#
#     a = int(input("A:"))
#     b = int(input("B:"))
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("Sonni 0 ga bolish mumkin emas")
#     else:
#         print(result)
#     finally:
#         print("Bajarildi")


# try :
#
#     a = int(input("Fayl nomi"))
#     with open(f'"{a}.txt", "r" ') as file:
#         file.read()
# except FileNotFoundError:
#         print("Bu nomli fayl mavjud emas")
# else:
#      file.read()
# finally:
#         print("Finish")

class Person:
    def __init__(self, name, age, surname, city):
        self.name = name
        self.age = age
        self.surname = surname
        self.city = city

    def info_person(self):
        return f"{self.name}\n{self.surname}\n{self.age}\n{self.city}"

    def get_year(self):
        import datetime
        today = datetime.date.today()
        year = today.year
        return year-int(self.age)


# p1 = Person('Shaxriyor', 22, 'Sharofov', 'Buxoro')
# # print(p1.info_person())
# print(p1.get_year())


class Student(Person):
    def __init__(self, name, age, surname, city, university, course, prof):
        super().__init__(name, age, surname, city)
        self.university = university
        self.course = course
        self.prof = prof

    def get_univer_info(self):
        return self.university, self.course, self.prof

s1 = Student('Shaxriyor', 22, 'Sharofov', 'Buxoro', 'TDTU', 4, 'KIF')

print(s1.get_univer_info())
print(s1.get_year())
print(s1.info_person())



# class Computer:
#     def __init__(self, monitor, keyboard, cursor, memory):
#         self.monitor = monitor
#         self.keyboard = keyboard
#         self.cursor = cursor
#         self.memory = memory
#     def get_LapTop_info(self):
#
#
#         return self.monitor, self.cursor
#
#
#
#
#
#
# LapTop = Computer("13inch", "white colour", "touch bat", "256GB")
# print(LapTop.get_LapTop_info())





































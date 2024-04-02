# class Animal :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info_animal(self):
#         return f"Name:{self.name}\nAge:{self.age}"
#
#
#
#
#
# class Zoo :
#     num_animals = 0
#     def __init__(self, name_zoo, shahar):
#         self.name_zoo = name_zoo
#         self.shahar = shahar
#         self.animals = []
#         Zoo.num_animals += 1
#
#     def add_animal(self):
#         self.animals.append(Animal())




import csv

data = [['Name', 'Age'], ['Alex', '20'], ['Bob', '25']]

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data)

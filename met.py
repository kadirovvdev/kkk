# class Animals:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#
#
#     def info_Animal(self):
#         return f"{self.name}\n{self.type}"
#
#
# a1 = Animals("bear", "gosht")
# print(a1.info_Animal)
#
#
# class Zoo:
#     num_animals = 0
#     def __init__(self, name_zoo, shahar):
#         self.name_zoo = name_zoo
#         self.shahar = shahar
#         self.animals = []
#         num_animals.Zoo =

class Ice_cream:
    def __init__(self, make, color, price):
        self.make = make
        self.color = color
        self.price = price

    def get_ice_cream_info(self):
        return f"Make:{self.make}\nColor:{self.color}\nPrice:{self.price}"

# a1 = Ice_cream("Banana", "Yellow", "2$")
# print(a1.__dict__)
# print(a1.get_ice_cream_info())

# a = dir(Ice_cream)
# for i in a:
#     if i[:2] != "__":
#         print(i)


class MusqaymoqXona:
    num_ice_cream = 0

    def __init__(self, name):
        self.name = name
        self.marujnalar = []
        MusqaymoqXona.num_ice_cream += 1

    def __str__(self):
        return self.name

    def add_ice_cream(self, ice_cream):
        if isinstance(ice_cream, Ice_cream):
            self.marujnalar.append(ice_cream)
        else:
            print("Marujna classga doir emas")

    def get_ice_creams(self):
        return [i.get_ice_cream_info().split('\n') for i in self.marujnalar]

    def count_ice_cream(self):
        return len([i.get_ice_cream_info().split('\n') for i in self.marujnalar])

    def get_details_marujnalar(self, i):
        try:
            my_ice_creams = [i.get_ice_cream_info().split('\n') for i in self.marujnalar]
            s = my_ice_creams[i - 1]
        except IndexError:
            return "Marujnaxonada bunaqa marujna yo'q"
        else:
            return s

    def update_ice_cream(self, i, new_ice_cream):
        if i < 1:
            return "Marujnaxonada bunday marujna yo'q"
        elif i > len(self.marujnalar):
             self.marujnalar.append(new_ice_cream)
             return "Yangi marujna qo'shildi. Bunday id bo'lmagani uchun"
        else:
            self.marujnalar[i-1] = new_ice_cream
            return "O'zgardi"

    @classmethod
    def get_num_ice_cream(cls):
        return cls.num_ice_cream

    @staticmethod
    def get_address(vil, tum):
        return f"{vil}, {tum}"

dokan1 = MusqaymoqXona("Mega")
dokan2 = MusqaymoqXona("Anjan marujnalari")

a1 = Ice_cream("Banana", "Yellow", "2$")
a2 = Ice_cream("Chokolate", "Black", "3$")
a3 = Ice_cream("Vanil", "Orange", "4$")
a4 = Ice_cream("Milk", "White", "1$")

dokan1.add_ice_cream(a1)
dokan1.add_ice_cream(a2)

dokan2.add_ice_cream(a3)
dokan2.add_ice_cream(a4)

# print(dokan2.get_ice_creams())
# print(dokan2.count_ice_cream())
#
# print(dokan2.get_details_marujnalar(2))
# print(dokan2.update_ice_cream(2, a3))
# print(dokan2.update_ice_cream(2, a4))
# print(dokan2.get_ice_creams())
# print(MusqaymoqXona.get_num_ice_cream())
# print(MusqaymoqXona.get_address("Farg'ona", "Oltiariq"))

with open ("books", "w") as file:
    for i in range(1,len(dokan2.get_ice_creams())):
        file.write(f"{i}    {dokan2.get_ice_creams()}\n")

# import csv
#
# FILENAME = input('File nomini kiriting:')
#
# users = [
#     ["Ali", 25],
#     ["Sobir", 32],
#     ["Dilnoza", 14],
#     ['Obidjon', 22]
#
# ]
#
# with open(f"{FILENAME}.csv", "w", newline="") as fayl:
#     writer = csv.writer(fayl)
#     writer.writerows(users)
#
#
# with open(f"{FILENAME}.csv", "a", newline="") as fayl:
#     user = ["Shaxnoza", 18]
#     writer = csv.writer(fayl)
#     writer.writerow(user)
#
#
# import csv
#
#
# FILENAME = "usersd.csv"
#
#
# users = [
#     {"ism": "Ali", "yosh": 25},
#     {"ism": "Sobir", "yosh": 32},
#     {"ism": "Dilnoza", "yosh": 14}
#
# ]
#
# with open(FILENAME, "w", newline="") as fayl:
#     ustunlar = ["ism", "yosh"]
#     writer = csv.DictWriter(fayl, fieldnames=ustunlar)
#     writer.writeheader()
#     # bir qancha qatorlarni yozish
#     writer.writerows(users)
#
#     user = {"ism": "Shaxnoza", "yosh": 18}
#     # bitta qatorni yozish
#     writer.writerow(user)
#
#
# FILENAME = input('File nomini kiriting:')
#
# try:
#     with open(f'{FILENAME}.csv', "r", newline="") as fayl:
#         reader = csv.DictReader(fayl)
#         for row in reader:
#             a = row["ism"], "-", row["yosh"]
#             print(a)
# except FileNotFoundError:
#     print('Bunqa file mavjud emas')
# except KeyError:
#     print('Dict da yozilmagan malumotlar')
#
#
# FILENAME = input('File nomini kiriting:')
#
# try:
#     fayl = open(f'{FILENAME}.csv', "r", newline="")
#     reader = csv.DictReader(fayl)
#     for row in reader:
#         a = row["ism"], "-", row["yosh"]
#         print(a)
# except FileNotFoundError:
#     print('Bunqa file mavjud emas')
# except KeyError:
#     print('Dict da yozilmagan malumotlar')
# except NameError:
#     print('Xato nom kiritildi')
# finally:
#     try:
#         fayl.close()
#     except NameError:
#         print('xato nom')
#
#
# import os
#
# os.mkdir('/home/waxento/Desktop/hello.txt')
# os.remove('/home/waxento/Desktop/text.csv')
# os.rename('/home/waxento/Desktop/hello.txt', '/home/waxento/Desktop/hellooo.txt')
#
#
# filename = input ("Faylning yo'lini kiriting:")
# if os.path.exists(filename):
#     print("ko'rsatilgan fayl mavjud")
#
# else:
#     print("Fayl mavjud emas")
#
# k = int(input('Takrorlanishlar soni:'))
# for i in range(k):
#     a = int(input('A:'))
#     b = int(input('B:'))
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print('Sonni 0 ga bolish mkn emas.')
#     else:
#         print(result)
#     finally:
#         print('Bajarildi')
#
#
# k = int(input('Takrorlanishlar soni:'))
# for i in range(k):
#
#     try:
#         a = int(input('A:'))
#         b = int(input('B:'))
#         result = a/b
#     # except ZeroDivisionError:
#     #     print('Sonni 0 ga bolish mkn emas.')
#     # except ValueError as e:
#     #     print('Siz int kiritishingiz kk', e)
#     except Exception as e:
#         print(f"Xatolik\n{e}")
#     else:
#         print(result)
#     finally:
#         print('Bajarildi')
#
#
# import csv
#
# oooo="nmadr.csv"
#
# with open(oooo, 'r', newline="") as nmadrfile:
#     yanginmadr=csv.reader(nmadrfile)
#     for qator in yanginmadr:
#         print(qator)

# from faker import Faker
# import random
#
# fake = Faker()
#
#
# with open ("Name.txt", "w") as name, open("age.txt", "w") as age, open  ("result.txt", "w") as result:
#     for i in range(1,50):
#         name.write(f"{i} {fake.name()}\n")
#         age.write(f"{i}  {2024-int(fake.year())}\n")
#         result.write(f"{i} {fake.name()}  {2024-int(fake.year())}\n")
#         # result.write(f"{i} {fake.name()}  {random.randint(1,50)}\n")


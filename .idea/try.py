

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
# except ValueErrorwdwe:
#         print("Bu nomli fayl mavjud emas")
# else:
#      file.read()
# finally:
#         print("Finish")

# a = []
# b = []
# try:
#     for i in a:
#
# except IndexError:
#     print("Element mavjud emas")
# else:
#     b.append(a[i])
#
# finally:
#     print("tugadi")




# import csv
# Filename = "users.csv"
#
# FILENAME = "users.csv"
# users = [ ["Ali", 25],
# ["Sobir", 32],
# ["Dilnoza", 14]
# ]
# with open(Filename, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)





import csv
FILENAME = "users.csv"
with open(FILENAME, "r", newline="") as fayl:
    reader = csv.reader(fayl)
    for row in reader:
        print(row[0], " - ", row[1])





















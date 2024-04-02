import psycopg2
from faker import Faker
from prettytable import PrettyTable
fake = Faker()

conn = psycopg2.connect(dbname='n38', host='localhost', port='5433', user='postgres', password='1709')

curr = conn.cursor()

with open ('database.txt', 'a') as file:
    for i in range(1,10):
        file.write(f"{i} {fake.name()}\n")

table = PrettyTable()

table.field_names = ["ID", "NAME"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])

# data = [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],

     # ]





# .txt fayldan malumotlarni o'qish
def read_data_from_txt(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    return data

# .txt fayldan malumotlarni o'qish
def print_table_from_txt(filename):
    data = read_data_from_txt(filename)
    table = PrettyTable(["Name", "Age", "City"])
    for row in data:
        table.add_row(row)
    print(table)

# Test
print_table_from_txt("database.txt")


























conn.commit()
conn.close()
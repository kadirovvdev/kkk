import psycopg2
conn = psycopg2.connect(dbname='python3', host='localhost', port='5433', user='postgres', password='1709')

curr = conn.cursor()


from prettytable import PrettyTable

table = PrettyTable()


table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])

data = [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]

table.add_rows(
   data
)


print(table)
for i in data:
    print(f"{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n")


############################################################################################################


from prettytable import PrettyTable

def print_table(data):
    table = PrettyTable()
    table.field_names = ["Name", "Age", "City"]
    for row in data:
        table.add_row(row)
    print(table)








def write_to_file(data, filename):
    with open(filename, 'w') as f:
        for row in data:
            f.write(','.join(row) + '\n')











def read_from_file(filename):
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip().split(','))
    return data











# def insert_into_table(table, row):
#     table.add_row(row)



def insert_func(table_name):
    table_name1 = input('table nomini kiriting:')
    curr.execute(f"SELECT *from {table_name}")
    c_name = [i[0] for i in curr.description]
    input_data = [input(f"{i} ni kiriting:") for i in c_name]
    curr.execute(f"insert into {table_name} values {tuple(input_data)}")







def print_from_file(filename):
    data = read_from_file(filename)
    print_table(data)













































conn.commit()
conn.close()
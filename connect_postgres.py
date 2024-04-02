import psycopg2
conn = psycopg2.connect(dbname='python3', host='localhost', port='5433', user='postgres', password='1709')

curr = conn.cursor()

# def create_table(table_name):
#     try:
#         curr.execute(f'create table {table_name} (id serial primary key, name varchar(20))')
#     except Exception:
#         print(f'Table {table_name} already exists')
#     else:
#         print(f'Table {table_name} created')
# create_table('users')




# def drop_table(table_name):
#     try:
#         curr.execute(f'drop table {table_name}')
#     except Exception:
#         print(f'Table {table_name} does not exist')
#     else:
#         print(f'Table {table_name} dropped')
# drop_table('users')



# def add_column(table_name, column_name, data_type, exc=''):
#     try:
#         curr.execute(f'alter table {table_name} add column {column_name} {data_type} {exc}')
#     except Exception as a:
#         print(f'Column {column_name} already exists{a}')
#     else:
#         print(f'Column {column_name} added')
# add_column('cars', 'modell123', 'varchar')

# def drop_column(table_name, column_name):
#     try:
#         curr.execute(f'alter table {table_name} drop column {column_name}')
#     except Exception as a:
#         print(f'Column {column_name} does not exist{a}')
#     else:
#         print(f'Column {column_name} dropped')
# drop_column('cars', 'model')
#
#
#
# def change_column_name(table_name, column_name):
#     try:
#         curr.execute(f'alter table {table_name} rename column {column_name} to {column_name}_new')
#     except Exception as a:
#         print(f'Column {column_name} does not exist{a}')
#     else:
#         print(f'Column {column_name} renamed')
#
# change_column_name('cars', 'model')
#
#
#
#
# def change_column_type(table_name, column_name, data_type):
#     try:
#         curr.execute(f'alter table {table_name} alter column {column_name} type {data_type}')
#     except Exception as a:
#         print(f'Column {column_name} does not exist{a}')
#     else:
#         print(f'Column {column_name} type changed')
#
# change_column_type('cars', 'model', 'varchar(20)')
#
#
#
# def insert_into_table(table_name):
#     try:
#         curr.execute(f'insert into {table_name} (name) values ("<NAME>")')
#     except Exception:
#         print(f'Table {table_name} already exists')
#     else:
#         print(f'Table {table_name} inserted')
# insert_into_table('cars')
#
#
# def update_(table_name):
#     try:
#         curr.execute(f'update {table_name} set name = "<NAME>"')
#     except Exception:
#         print(f'Table {table_name} does not exist')
#     else:
#         print(f'Table {table_name} updated')
# update_(table_name=)


def rename_table(table_name):
    try:
        curr.execute(f'alter table {table_name} rename to {table_name}_new')
    except Exception:
        print(f'Table {table_name} does not exist')
    else:
        print(f'Table {table_name} renamed')
rename_table(table_name=)











conn.commit()
conn.close()




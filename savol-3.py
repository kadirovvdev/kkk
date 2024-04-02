import sqlite3
import psycopg2


conn = psycopg2.connect(dbname='n38', host='localhost', port='5433', user='postgres', password='1709')

curr = conn.cursor()

def create_database_table():

    db_name = input("Malumotlar bazasini nomini kiriting: ")


    table_name = input("Table nomini kiriting: ")

    try:

        conn = sqlite3.connect(db_name)
        cur = conn.cursor()


        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        existing_table = cur.fetchone()
        if existing_table:
            print("Bunaqa malumotlar bazasida table bor")
        else:

            cur.execute(f'''CREATE TABLE {table_name} (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER,
                            country TEXT
                        )''')
            print("Table muvaffaqiyatli yaratildi")


        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Xatolik yuz berdi:", e)

def drop_table():

    db_name = input("Malumotlar bazasini nomini kiriting: ")


    table_name = input("Ochiriladigan table nomini kiriting: ")

    try:

        conn = sqlite3.connect(db_name)
        cur = conn.cursor()


        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        existing_table = cur.fetchone()
        if existing_table:

            cur.execute(f"DROP TABLE {table_name}")
            print("Table muvaffaqiyatli o'chirildi")
        else:
            print("Bunaqa table yo'q")


        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Xatolik yuz berdi:", e)


if __name__ == "__main__":
    print("1. Malumotlar bazasini yaratish va table yaratish")
    print("2. Tableni o'chirish")
    choice = input("Tanlang (1 yoki 2): ")

    if choice == "1":
        create_database_table()
    elif choice == "2":
        drop_table()
    else:
        print("Noto'g'ri tanlov")

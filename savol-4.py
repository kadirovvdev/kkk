import sqlite3
import psycopg2


conn = psycopg2.connect(dbname='n38', host='localhost', port='5433', user='postgres', password='1709')

curr = conn.cursor()

def delete_user():

    db_name = input("Malumotlar bazasini nomini kiriting: ")

    try:

        conn = sqlite3.connect(db_name)
        cur = conn.cursor()


        user_id = int(input("O'chiriladigan foydalanuvchi ID sini kiriting: "))


        cur.execute(f"SELECT * FROM users WHERE id = ?", (user_id,))
        user = cur.fetchone()
        if user:
            cur.execute(f"DELETE FROM users WHERE id = ?", (user_id,))
            print(f"Foydalanuvchi {user_id} muvaffaqiyatli o'chirildi")
        else:
            print("Bu user bizda mavjud emas")


        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print("Xatolik yuz berdi:", e)


if __name__ == "__main__":
    delete_user()

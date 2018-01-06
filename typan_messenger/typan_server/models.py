import sqlite3
import os

root = os.path.abspath('.')
db_path = os.path.join(root, 'server.db')
conn = sqlite3.connect(db_path)

c = conn.cursor()


def create_table():
    try:
        c.execute('''CREATE TABLE user
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                         login TEXT NOT NULL, 
                         info TEXT)''')
        c.execute('''CREATE TABLE history 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                         time TEXT NOT NULL,
                         ip_addr TEXT NOT NULL,
                         FOREIGN KEY (id) REFERENCES user(id))''')
        c.execute('''CREATE TABLE contacts
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                         id_contact INTEGER NOT NULL,
                         FOREIGN KEY (id) REFERENCES user(id),
                         FOREIGN KEY (id_contact) REFERENCES user(id))''')
    except Exception as err:
        print('ERROR {} {}'.format(type(err), err))
        os.remove(db_path)
    else:
        conn.commit()
    finally:
        conn.close()
        print('DataBase was successfully created!')


def new_user():
    pass


def new_history():
    pass


def new_contact():
    pass


def get_user():
    pass


def get_history():
    pass


def get_contacts():
    pass

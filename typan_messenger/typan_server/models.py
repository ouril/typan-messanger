import sqlite3
import os

root = os.path.abspath('.')
db_path = os.path.join(root, 'server.db')


def create_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE user
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                         login TEXT NOT NULL UNIQUE, 
                         info TEXT)''')
        c.execute('''CREATE TABLE history 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                         time TEXT NOT NULL,
                         ip_addr TEXT NOT NULL,
                         FOREIGN KEY (id) REFERENCES user(id))''')
        c.execute('''CREATE TABLE contacts
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                         FOREIGN KEY (id) REFERENCES user(id),
                         FOREIGN KEY (id_contact) REFERENCES user(id))''')
    except Exception as err:
        print('ERROR {} {}'.format(type(err), err))
        os.remove(db_path)
        conn.close()
    else:
        conn.commit()
    finally:
        conn.close()
        print('DataBase was successfully created!')


def new_info(sql, params):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        c.execute(sql, params)
    except Exception as err:
        print('ERROR {} {}'.format(type(err), err))
    else:
        conn.commit()
    finally:
        conn.close()


def sql_insert(tb, params, values):
    return 'INSERT INTO {} ({}) VALUES ({})'.format(tb, params, values)


def get_info(sql, params):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        c.execute(sql, params)
    except Exception as err:
        print('ERROR {} {}'.format(type(err), err))
    else:
        res = c.fetchall()
    finally:
        conn.close()
        return res


def sql_insert(params, tb):
    return 'SELECT {} FROM {}'.format(params, tb)

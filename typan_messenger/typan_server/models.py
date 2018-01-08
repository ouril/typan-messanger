import sqlite3
import os


class ServerDB:

    def __init__(self, name_db='server.db'):
        self.root = os.path.abspath('.')
        self.db_path = os.path.join(self.root, name_db)

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
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
                             id_user INTEGER NOT NULL,
                             id_contact INTEGER NOT NULL, 
                             FOREIGN KEY (id_user) REFERENCES user(id),
                             FOREIGN KEY (id_contact) REFERENCES user(id))''')
        except Exception as err:
            print('ERROR {} {}'.format(type(err), err))
            os.remove(db_path)
            conn.close()
        else:
            conn.commit()
            print('DataBase was successfully created!')
        finally:
            conn.close()

    def new_info(self, sql, params=None):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        try:
            if params:
                c.execute(sql, params)
            else:
                c.execute(sql)
        except Exception as err:
            print('ERROR {} {}'.format(type(err), err))
        else:
            conn.commit()
        finally:
            conn.close()

    def sql_insert(self, tb, params, values):
        return 'INSERT INTO {} ({}) VALUES ({})'.format(tb, params, values)

    def get_info(sql, params=None):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        try:
            if params:
                c.execute(sql, params)
            else:
                c.execute(sql)
            res = c.fetchall()
        except Exception as err:
            print('ERROR {} {}'.format(type(err), err))
        else:
            if len(res) == 1:
                return res[0]
            else:
                return res
        finally:
            conn.close()

    def sql_get(self, params, tb, where):
        return 'SELECT {} FROM {} WHERE {}'.format(params, tb, where)

    def get_user_id(self, user):
        id_sql = self.sql_get('id', 'user', f"login = '{user}'")
        id = self.get_info(id_sql)
        sql = '''SELECT login, info FROM contacts c, user u WHERE c.id_contact = {}
            '''.format(id[0])
        return sql

    def get_contact_list(self, user):
        sql = self.get_user_id(user)
        return self.get_info(sql)

    def add_user_to_base(self, contact):
        value = "('{}', '{}')".format(contact[0], contact[1])
        sql = self.sql_insert('user', 'login, info', value)
        self.new_info(sql)

    def add_contact_to_base(self, contact_name, user):
        id_user = self.get_user_id(user)
        id_contact = self.get_user_id(contact_name)
        if id_contact:
            value = "({}, {})".format(id_user, id_contact)
            sql = self.sql_insert('contact', 'id_user, id_contact', value)
            self.new_info(sql)

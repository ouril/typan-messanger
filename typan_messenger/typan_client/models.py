from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField

db = SqliteDatabase('client.db')


class Messages(Model):
    name = CharField()

    class Meta:
        database = db


class Contacts(Model):
    pass
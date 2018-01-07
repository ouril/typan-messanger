import os
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    IntegerField,
    BooleanField,
    DateTimeField
)

db = SqliteDatabase('client.db')


class Messages(Model):
    message = CharField(null=True, verbose_name='Message')
    action = CharField(verbose_name='Action')
    to = CharField(verbose_name='To contact')
    date = DateTimeField(verbose_name='Date of created')
    response = BooleanField(verbose_name='Is successes', default=True)

    class Meta:
        database = db


class Contacts(Model):
    name = CharField(verbose_name='Contact name', unique=True)
    info = CharField(verbose_name='info about contact', null=True)

    class Meta:
        database = db


def create_client_db():
    try:
        db.connect()
        db.create_table([Messages, Contacts], safe=True)
    except Exception as err:
        print(err)
        os.remove('client.db')
    else:
        print('Client db was successfully created')
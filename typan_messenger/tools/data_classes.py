import collections as cl
from collections.abc import Collection


Contact = cl.namedtuple('Contact', ['name', 'info'])


class BaseContactList(Collection):

    def __init__(self, user):
        self.user = user
        self.contacts = []

    def __contains__(self, item):
        for i in self.contacts:
            if item == i.name:
                return True

    def __getitem__(self, key):
        return self.contacts[key]

    def __len__(self):
        return len(self.contacts)

    def __iter__(self):
        for i in self.contacts:
            yield i

    def add_contact(self, contact, info):
        cont = Contact(name=contact, info=info)
        self.contacts.append(cont)
        return cont

    def find(self, name):
        """
        Find by name
        :param name: str
        :return: namedtaple of contact
        """
        for i in self.contacts:
            if i.name == name:
                return i

    def delete_contact(self, name):
        name_for_del = ''
        for i in self.contacts:
            if i.name == name:
                name_for_del = i.name
                del i
        return name_for_del

    def for_encoding(self):
        return (dict(i._asdict()) for i in self.contacts)

    @classmethod
    def build(cls, data, user):
        """
        For building after encoding
        :param data: data like list with dicts inside. in each dict must be name and info keys
        :param user: name of contact list
        :return: obj of self
        """
        contact_list = cls(user)
        for i in data:
            contact_list.add_contact(i.get('name'), i.get('info'))
        return contact_list

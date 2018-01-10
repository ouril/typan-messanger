from typan_messenger.tools.data_classes import BaseContactList
from .models import ServerDB


class ServerContactList(BaseContactList):

    def __init__(self, user):
        super(ServerContactList, self).__init__(user)
        self.db = ServerDB

    def clean(self):
        for i in self.contacts:
            del i

    @classmethod
    def build_from_base(cls, user):
        contact_list = cls(user)
        try:
            contacts = contact_list.db.get_contact_list(user)
        except Exception as err:
            print(err)
        else:
            contact_list = cls(user)
            for contact in contacts:
                contact_list.add_contact(contact[0], contact_list[1])
            return contact_list

    def add_contact(self, contact_name, info):
        super(ServerContactList, self).add_contact(contact_name, info)
        self.db.add_contact_to_base(contact_name, self.user)

    def delete_contact(self, contact_name):
        self.db.delete_contact(contact_name, self.user)
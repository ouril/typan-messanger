from typan_messenger.tools.data_classes import BaseContactList


class ClientContactList(BaseContactList):

    def clean(self):
        for i in self.contacts:
            del i

    @classmethod
    def build_from_base(cls):
        pass

    def update_base(self):
        pass
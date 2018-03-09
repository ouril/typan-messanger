import sys
from PyQt5 import QtWidgets
from .typan_msg import *
from .client import Client
from typan_messenger.tools.command_tools import run_client


class GuiClient(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        self.client = Client()
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Cancel.clicked.connect(lambda: self.client.disconnect_server())
        self.ui.ok.clicked.connect(lambda: self.client.login())

        self.ui.send.clicked.connect(lambda: self.client.send_msg())
        self.ui.textEdit.cursorPositionChanged.connect(lambda: print(self.ui.textEdit.plainText))

    def exit(self):
        self.client.disconnect_server()
        QtWidgets.qApp.quit()

    def start(self):
        self.client.login()



def run_client_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = GuiClient()
    window.show()
    sys.exit(app.exec_())

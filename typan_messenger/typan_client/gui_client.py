import sys
from PyQt5 import QtWidgets
from .typan_msg import *
from typan_messenger.tools.command_tools import run_client


class GuiClient(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Cancel.clicked.connect(QtWidgets.qApp.quit)
        #run_client()


def run_client_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = GuiClient()
    window.show()
    sys.exit(app.exec_())

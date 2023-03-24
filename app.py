import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.graphWidget1.plot()
        self.graphWidget2.plot()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

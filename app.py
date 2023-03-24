import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from table import TableModel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.tableView.setModel(self.model)

        self.ageGraphWidget.plot()
        self.ageRegionGraphWidget.plot()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

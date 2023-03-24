import sys
from PyQt5 import QtWidgets
import seaborn as sns

from mplwidget import MplWidget

sns.set_theme()


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Create the matplotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        w = MplWidget()
        # Create data
        x = range(1, 6)
        y1 = [1, 4, 6, 8, 9]
        y2 = [2, 2, 7, 10, 12]
        y3 = [2, 8, 5, 10, 6]
        w.canvas.axes.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'])
        w.canvas.axes.legend(loc='upper left')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(w)

        # Create a placeholder widget to hold out toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()

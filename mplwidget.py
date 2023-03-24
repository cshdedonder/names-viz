import matplotlib
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns

matplotlib.use('Qt5Agg')
sns.set_theme()


# Matplotlib canvas
class MplCanvas(FigureCanvas):

    def __init__(self):
        self.fig = Figure(figsize=(5, 2.1), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.fig.tight_layout()
        super(MplCanvas, self).__init__(self.fig)
        # FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


# Matplotlib Widget
class MplWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

import mplwidget


class AgeGraphWidget(mplwidget.MplWidget):

    def __init__(self, parent=None):
        super(AgeGraphWidget, self).__init__(parent)

    def plot(self, name=None):
        x = range(1, 6)
        y1 = [1, 4, 6, 8, 9]
        y2 = [2, 2, 7, 10, 12]
        y3 = [2, 8, 5, 10, 6]
        self.canvas.axes.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'])
        self.canvas.axes.legend(loc='upper left')


class AgeRegionGraphWidget(mplwidget.MplWidget):

    def __init__(self, parent=None):
        super(AgeRegionGraphWidget, self).__init__(parent)

    def plot(self, name=None):
        x = range(1, 6)
        y1 = [1, 4, 6, 8, 9]
        y2 = [2, 2, 7, 10, 12]
        y3 = [2, 8, 5, 10, 6]
        self.canvas.axes.stackplot(x, y1, y2, y3, labels=['D', 'F', 'G'])
        self.canvas.axes.legend(loc='upper left')

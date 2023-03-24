from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QModelIndex


# noinspection PyMethodOverriding
class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self.data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.data[0])

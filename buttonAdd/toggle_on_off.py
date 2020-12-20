import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 350)
        MainWindow.setMinimumSize(QtCore.QSize(550, 350))
        MainWindow.setMaximumSize(QtCore.QSize(550, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 500, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_Save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Save.setGeometry(QtCore.QRect(120, 250, 100, 50))
        self.pushButton_Save.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_Save.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_Save.setObjectName("pushButton_Save")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Filter"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "complement"))
        self.pushButton_Save.setText(_translate("MainWindow", "Save"))
        self.pushButton_Save.clicked.connect(self.bindSave)

    def bindSave(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)

        groupButton = QtWidgets.QButtonGroup(self.tableWidget)
        groupButton.setExclusive(True)
        it1 = QtWidgets.QTableWidgetItem("filter " + str(numRows))
        self.tableWidget.setItem(numRows, 0, it1)
        ch_bx1 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx1)
        self.tableWidget.setCellWidget(numRows, 1, ch_bx1)
        ch_bx2 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx2)
        self.tableWidget.setCellWidget(numRows, 2, ch_bx2)


if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

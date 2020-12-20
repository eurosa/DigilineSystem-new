#import os
#os.system("C:\Python37\python -m PyQt5.uic.pyuic -x  beta.ui -o beta_gui.py")
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from beta_gui import Ui_MainWindow  # importing our generated file

import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.AddButton)
        self.num = 3

        self.layout = QtWidgets.QVBoxLayout(self.ui.centralwidget)
        self.layout.addWidget(self.ui.pushButton)
        self.layout.addWidget(self.ui.pushButton_2)

    def AddButton(self, result):
        button = QtWidgets.QPushButton("button {}".format(self.num))
        button.clicked.connect(lambda: print(button.text()))
        self.layout.addWidget(button)
        self.num += 1

#        try:
#        self.ui.pushButton_3 = QtWidgets.QPushButton(self.ui.centralwidget)
#        self.ui.pushButton_3.setGeometry(QtCore.QRect(0, 0, 75, 23))
#        self.ui.pushButton_3.setObjectName("pushButton_3")
#        self.ui.pushButton_3.setText("buton_3")
#        self.update()
#        print(self.ui.pushButton_3.text())
#        self.show()
#        except Exception as e:
#            print(e)
#        return


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())


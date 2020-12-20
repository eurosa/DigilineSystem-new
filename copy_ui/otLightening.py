# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otLightening.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 386)
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lightLabel1 = QtWidgets.QLabel(Form)
        self.lightLabel1.setMinimumSize(QtCore.QSize(91, 19))
        self.lightLabel1.setMaximumSize(QtCore.QSize(91, 19))
        self.lightLabel1.setObjectName("lightLabel1")
        self.gridLayout_5.addWidget(self.lightLabel1, 0, 0, 1, 1)
        self.lightLabel2 = QtWidgets.QLabel(Form)
        self.lightLabel2.setMinimumSize(QtCore.QSize(91, 19))
        self.lightLabel2.setMaximumSize(QtCore.QSize(91, 19))
        self.lightLabel2.setObjectName("lightLabel2")
        self.gridLayout_5.addWidget(self.lightLabel2, 0, 1, 1, 1)
        self.lightLabel3 = QtWidgets.QLabel(Form)
        self.lightLabel3.setMinimumSize(QtCore.QSize(41, 19))
        self.lightLabel3.setMaximumSize(QtCore.QSize(41, 19))
        self.lightLabel3.setObjectName("lightLabel3")
        self.gridLayout_5.addWidget(self.lightLabel3, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lightBulb1 = QtWidgets.QLabel(Form)
        self.lightBulb1.setMinimumSize(QtCore.QSize(41, 41))
        self.lightBulb1.setMaximumSize(QtCore.QSize(41, 41))
        self.lightBulb1.setStyleSheet("QLabel { \n"
"color: #000000; \n"
"}")
        self.lightBulb1.setText("")
        self.lightBulb1.setPixmap(QtGui.QPixmap("icon/light-bulb.png"))
        self.lightBulb1.setScaledContents(True)
        self.lightBulb1.setObjectName("lightBulb1")
        self.gridLayout.addWidget(self.lightBulb1, 0, 0, 1, 1)
        self.toggleContainerGasL1 = QtWidgets.QWidget(Form)
        self.toggleContainerGasL1.setMinimumSize(QtCore.QSize(111, 51))
        self.toggleContainerGasL1.setMaximumSize(QtCore.QSize(111, 51))
        self.toggleContainerGasL1.setObjectName("toggleContainerGasL1")
        self.gridLayout.addWidget(self.toggleContainerGasL1, 0, 1, 1, 1)
        self.lightBulb2 = QtWidgets.QLabel(Form)
        self.lightBulb2.setMinimumSize(QtCore.QSize(41, 41))
        self.lightBulb2.setMaximumSize(QtCore.QSize(41, 41))
        self.lightBulb2.setStyleSheet("QLabel { \n"
"color: #000000; \n"
"}")
        self.lightBulb2.setText("")
        self.lightBulb2.setPixmap(QtGui.QPixmap("icon/light-bulb.png"))
        self.lightBulb2.setScaledContents(True)
        self.lightBulb2.setObjectName("lightBulb2")
        self.gridLayout.addWidget(self.lightBulb2, 0, 2, 1, 1)
        self.toggleContainerGasL2 = QtWidgets.QWidget(Form)
        self.toggleContainerGasL2.setMinimumSize(QtCore.QSize(111, 51))
        self.toggleContainerGasL2.setMaximumSize(QtCore.QSize(111, 51))
        self.toggleContainerGasL2.setObjectName("toggleContainerGasL2")
        self.gridLayout.addWidget(self.toggleContainerGasL2, 0, 3, 1, 1)
        self.otLightBulb1 = QtWidgets.QLabel(Form)
        self.otLightBulb1.setMinimumSize(QtCore.QSize(31, 31))
        self.otLightBulb1.setMaximumSize(QtCore.QSize(31, 31))
        self.otLightBulb1.setStyleSheet("QLabel { \n"
"color: #000000; \n"
"}")
        self.otLightBulb1.setText("")
        self.otLightBulb1.setPixmap(QtGui.QPixmap("icon/lights.png"))
        self.otLightBulb1.setScaledContents(True)
        self.otLightBulb1.setObjectName("otLightBulb1")
        self.gridLayout.addWidget(self.otLightBulb1, 0, 4, 1, 1)
        self.toggleContainerOT1 = QtWidgets.QWidget(Form)
        self.toggleContainerOT1.setMinimumSize(QtCore.QSize(111, 51))
        self.toggleContainerOT1.setMaximumSize(QtCore.QSize(111, 51))
        self.toggleContainerOT1.setObjectName("toggleContainerOT1")
        self.gridLayout.addWidget(self.toggleContainerOT1, 0, 5, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.light2Decrement = QtWidgets.QPushButton(Form)
        self.light2Decrement.setMinimumSize(QtCore.QSize(31, 31))
        self.light2Decrement.setMaximumSize(QtCore.QSize(31, 31))
        self.light2Decrement.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light2Decrement.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/round_minus_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light2Decrement.setIcon(icon)
        self.light2Decrement.setObjectName("light2Decrement")
        self.gridLayout_3.addWidget(self.light2Decrement, 0, 12, 1, 1)
        self.light1_1 = QtWidgets.QLabel(Form)
        self.light1_1.setMinimumSize(QtCore.QSize(8, 23))
        self.light1_1.setMaximumSize(QtCore.QSize(8, 23))
        self.light1_1.setStyleSheet("QLabel{\n"
" border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
" \n"
"  min-height: 15px;\n"
" \n"
" max-height: 15px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_1.setText("")
        self.light1_1.setObjectName("light1_1")
        self.gridLayout_3.addWidget(self.light1_1, 0, 1, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_9 = QtWidgets.QLabel(Form)
        self.light2_9.setMinimumSize(QtCore.QSize(8, 63))
        self.light2_9.setMaximumSize(QtCore.QSize(8, 63))
        self.light2_9.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 55px;\n"
" \n"
" max-height:55px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_9.setText("")
        self.light2_9.setObjectName("light2_9")
        self.gridLayout_3.addWidget(self.light2_9, 0, 21, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_4 = QtWidgets.QLabel(Form)
        self.light2_4.setMinimumSize(QtCore.QSize(8, 38))
        self.light2_4.setMaximumSize(QtCore.QSize(8, 38))
        self.light2_4.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 30px;\n"
" \n"
" max-height:30px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_4.setText("")
        self.light2_4.setObjectName("light2_4")
        self.gridLayout_3.addWidget(self.light2_4, 0, 16, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_6 = QtWidgets.QLabel(Form)
        self.light1_6.setMinimumSize(QtCore.QSize(8, 48))
        self.light1_6.setMaximumSize(QtCore.QSize(8, 48))
        self.light1_6.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 40px;\n"
" \n"
" max-height:40px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_6.setText("")
        self.light1_6.setObjectName("light1_6")
        self.gridLayout_3.addWidget(self.light1_6, 0, 6, 1, 1, QtCore.Qt.AlignBottom)
        self.light1Increment = QtWidgets.QPushButton(Form)
        self.light1Increment.setMinimumSize(QtCore.QSize(0, 31))
        self.light1Increment.setMaximumSize(QtCore.QSize(31, 31))
        self.light1Increment.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light1Increment.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/plus_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light1Increment.setIcon(icon1)
        self.light1Increment.setObjectName("light1Increment")
        self.gridLayout_3.addWidget(self.light1Increment, 0, 11, 1, 1)
        self.light1Decrement = QtWidgets.QPushButton(Form)
        self.light1Decrement.setMinimumSize(QtCore.QSize(31, 31))
        self.light1Decrement.setMaximumSize(QtCore.QSize(31, 31))
        self.light1Decrement.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light1Decrement.setText("")
        self.light1Decrement.setIcon(icon)
        self.light1Decrement.setObjectName("light1Decrement")
        self.gridLayout_3.addWidget(self.light1Decrement, 0, 0, 1, 1)
        self.light1_3 = QtWidgets.QLabel(Form)
        self.light1_3.setMinimumSize(QtCore.QSize(8, 33))
        self.light1_3.setMaximumSize(QtCore.QSize(8, 33))
        self.light1_3.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 25px;\n"
" \n"
" max-height: 25px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_3.setText("")
        self.light1_3.setObjectName("light1_3")
        self.gridLayout_3.addWidget(self.light1_3, 0, 3, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_2 = QtWidgets.QLabel(Form)
        self.light2_2.setMinimumSize(QtCore.QSize(8, 28))
        self.light2_2.setMaximumSize(QtCore.QSize(8, 28))
        self.light2_2.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 20px;\n"
" \n"
" max-height: 20px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_2.setText("")
        self.light2_2.setObjectName("light2_2")
        self.gridLayout_3.addWidget(self.light2_2, 0, 14, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_5 = QtWidgets.QLabel(Form)
        self.light2_5.setMinimumSize(QtCore.QSize(8, 43))
        self.light2_5.setMaximumSize(QtCore.QSize(8, 43))
        self.light2_5.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 35px;\n"
" \n"
" max-height:35px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_5.setText("")
        self.light2_5.setObjectName("light2_5")
        self.gridLayout_3.addWidget(self.light2_5, 0, 17, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_6 = QtWidgets.QLabel(Form)
        self.light2_6.setMinimumSize(QtCore.QSize(8, 48))
        self.light2_6.setMaximumSize(QtCore.QSize(8, 48))
        self.light2_6.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 40px;\n"
" \n"
" max-height:40px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_6.setText("")
        self.light2_6.setObjectName("light2_6")
        self.gridLayout_3.addWidget(self.light2_6, 0, 18, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_4 = QtWidgets.QLabel(Form)
        self.light1_4.setMinimumSize(QtCore.QSize(8, 38))
        self.light1_4.setMaximumSize(QtCore.QSize(8, 38))
        self.light1_4.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 30px;\n"
" \n"
" max-height:30px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_4.setText("")
        self.light1_4.setObjectName("light1_4")
        self.gridLayout_3.addWidget(self.light1_4, 0, 4, 1, 1, QtCore.Qt.AlignBottom)
        self.light2Increment = QtWidgets.QPushButton(Form)
        self.light2Increment.setMinimumSize(QtCore.QSize(31, 31))
        self.light2Increment.setMaximumSize(QtCore.QSize(31, 31))
        self.light2Increment.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light2Increment.setText("")
        self.light2Increment.setIcon(icon1)
        self.light2Increment.setObjectName("light2Increment")
        self.gridLayout_3.addWidget(self.light2Increment, 0, 23, 1, 1)
        self.light2_3 = QtWidgets.QLabel(Form)
        self.light2_3.setMinimumSize(QtCore.QSize(8, 33))
        self.light2_3.setMaximumSize(QtCore.QSize(8, 33))
        self.light2_3.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 25px;\n"
" \n"
" max-height: 25px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_3.setText("")
        self.light2_3.setObjectName("light2_3")
        self.gridLayout_3.addWidget(self.light2_3, 0, 15, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_2 = QtWidgets.QLabel(Form)
        self.light1_2.setMinimumSize(QtCore.QSize(8, 28))
        self.light1_2.setMaximumSize(QtCore.QSize(8, 28))
        self.light1_2.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 20px;\n"
" \n"
" max-height: 20px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_2.setText("")
        self.light1_2.setObjectName("light1_2")
        self.gridLayout_3.addWidget(self.light1_2, 0, 2, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_9 = QtWidgets.QLabel(Form)
        self.light1_9.setMinimumSize(QtCore.QSize(8, 63))
        self.light1_9.setMaximumSize(QtCore.QSize(8, 63))
        self.light1_9.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 55px;\n"
" \n"
" max-height:55px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_9.setText("")
        self.light1_9.setObjectName("light1_9")
        self.gridLayout_3.addWidget(self.light1_9, 0, 9, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_1 = QtWidgets.QLabel(Form)
        self.light2_1.setMinimumSize(QtCore.QSize(8, 23))
        self.light2_1.setMaximumSize(QtCore.QSize(8, 23))
        self.light2_1.setStyleSheet("QLabel{\n"
" border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
" \n"
"  min-height: 15px;\n"
" \n"
" max-height: 15px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_1.setText("")
        self.light2_1.setObjectName("light2_1")
        self.gridLayout_3.addWidget(self.light2_1, 0, 13, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_7 = QtWidgets.QLabel(Form)
        self.light2_7.setMinimumSize(QtCore.QSize(8, 53))
        self.light2_7.setMaximumSize(QtCore.QSize(8, 53))
        self.light2_7.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 45px;\n"
" \n"
" max-height:45px;\n"
"   \n"
"  background-color:black;\n"
"}")
        self.light2_7.setText("")
        self.light2_7.setObjectName("light2_7")
        self.gridLayout_3.addWidget(self.light2_7, 0, 19, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_8 = QtWidgets.QLabel(Form)
        self.light1_8.setMinimumSize(QtCore.QSize(8, 58))
        self.light1_8.setMaximumSize(QtCore.QSize(8, 58))
        self.light1_8.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 50px;\n"
" \n"
"  max-height:50px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_8.setText("")
        self.light1_8.setObjectName("light1_8")
        self.gridLayout_3.addWidget(self.light1_8, 0, 8, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_10 = QtWidgets.QLabel(Form)
        self.light1_10.setMinimumSize(QtCore.QSize(8, 68))
        self.light1_10.setMaximumSize(QtCore.QSize(8, 68))
        self.light1_10.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 60px;\n"
" \n"
" max-height:60px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_10.setText("")
        self.light1_10.setObjectName("light1_10")
        self.gridLayout_3.addWidget(self.light1_10, 0, 10, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_10 = QtWidgets.QLabel(Form)
        self.light2_10.setMinimumSize(QtCore.QSize(8, 68))
        self.light2_10.setMaximumSize(QtCore.QSize(8, 68))
        self.light2_10.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 60px;\n"
" \n"
" max-height:60px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_10.setText("")
        self.light2_10.setObjectName("light2_10")
        self.gridLayout_3.addWidget(self.light2_10, 0, 22, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_5 = QtWidgets.QLabel(Form)
        self.light1_5.setMinimumSize(QtCore.QSize(8, 43))
        self.light1_5.setMaximumSize(QtCore.QSize(8, 43))
        self.light1_5.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 35px;\n"
" \n"
" max-height:35px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light1_5.setText("")
        self.light1_5.setObjectName("light1_5")
        self.gridLayout_3.addWidget(self.light1_5, 0, 5, 1, 1, QtCore.Qt.AlignBottom)
        self.light1_7 = QtWidgets.QLabel(Form)
        self.light1_7.setMinimumSize(QtCore.QSize(8, 53))
        self.light1_7.setMaximumSize(QtCore.QSize(8, 53))
        self.light1_7.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 45px;\n"
" \n"
" max-height:45px;\n"
"   \n"
"  background-color:black;\n"
"}")
        self.light1_7.setText("")
        self.light1_7.setObjectName("light1_7")
        self.gridLayout_3.addWidget(self.light1_7, 0, 7, 1, 1, QtCore.Qt.AlignBottom)
        self.light2_8 = QtWidgets.QLabel(Form)
        self.light2_8.setMinimumSize(QtCore.QSize(8, 58))
        self.light2_8.setMaximumSize(QtCore.QSize(8, 58))
        self.light2_8.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 50px;\n"
" \n"
"  max-height:50px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light2_8.setText("")
        self.light2_8.setObjectName("light2_8")
        self.gridLayout_3.addWidget(self.light2_8, 0, 20, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMinimumSize(QtCore.QSize(581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 3, 0, 1, 3)
        self.lightLabel4 = QtWidgets.QLabel(Form)
        self.lightLabel4.setMinimumSize(QtCore.QSize(81, 19))
        self.lightLabel4.setMaximumSize(QtCore.QSize(81, 19))
        self.lightLabel4.setObjectName("lightLabel4")
        self.gridLayout_5.addWidget(self.lightLabel4, 4, 0, 1, 1)
        self.lightLabel5 = QtWidgets.QLabel(Form)
        self.lightLabel5.setMinimumSize(QtCore.QSize(81, 19))
        self.lightLabel5.setMaximumSize(QtCore.QSize(81, 19))
        self.lightLabel5.setObjectName("lightLabel5")
        self.gridLayout_5.addWidget(self.lightLabel5, 4, 1, 1, 1)
        self.lightLabel6 = QtWidgets.QLabel(Form)
        self.lightLabel6.setMinimumSize(QtCore.QSize(67, 19))
        self.lightLabel6.setMaximumSize(QtCore.QSize(67, 19))
        self.lightLabel6.setObjectName("lightLabel6")
        self.gridLayout_5.addWidget(self.lightLabel6, 4, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lightBulb3 = QtWidgets.QLabel(Form)
        self.lightBulb3.setMinimumSize(QtCore.QSize(41, 41))
        self.lightBulb3.setMaximumSize(QtCore.QSize(41, 41))
        self.lightBulb3.setStyleSheet("QLabel { \n"
"color: #000000; \n"
"}")
        self.lightBulb3.setText("")
        self.lightBulb3.setPixmap(QtGui.QPixmap("icon/light-bulb.png"))
        self.lightBulb3.setScaledContents(True)
        self.lightBulb3.setObjectName("lightBulb3")
        self.gridLayout_2.addWidget(self.lightBulb3, 0, 0, 1, 1)
        self.toggleContainer = QtWidgets.QWidget(Form)
        self.toggleContainer.setMinimumSize(QtCore.QSize(111, 51))
        self.toggleContainer.setMaximumSize(QtCore.QSize(111, 51))
        self.toggleContainer.setObjectName("toggleContainer")
        self.gridLayout_2.addWidget(self.toggleContainer, 0, 1, 1, 1)
        self.lightBulb4 = QtWidgets.QLabel(Form)
        self.lightBulb4.setMinimumSize(QtCore.QSize(41, 41))
        self.lightBulb4.setMaximumSize(QtCore.QSize(41, 41))
        self.lightBulb4.setStyleSheet("QLabel { \n"
"color: #000000; \n"
"}")
        self.lightBulb4.setText("")
        self.lightBulb4.setPixmap(QtGui.QPixmap("icon/light-bulb.png"))
        self.lightBulb4.setScaledContents(True)
        self.lightBulb4.setObjectName("lightBulb4")
        self.gridLayout_2.addWidget(self.lightBulb4, 0, 2, 1, 1)
        self.toggleContainerLaminar = QtWidgets.QWidget(Form)
        self.toggleContainerLaminar.setMinimumSize(QtCore.QSize(111, 51))
        self.toggleContainerLaminar.setMaximumSize(QtCore.QSize(111, 51))
        self.toggleContainerLaminar.setObjectName("toggleContainerLaminar")
        self.gridLayout_2.addWidget(self.toggleContainerLaminar, 0, 3, 1, 1)
        self.otLightBulb2 = QtWidgets.QLabel(Form)
        self.otLightBulb2.setMinimumSize(QtCore.QSize(31, 31))
        self.otLightBulb2.setMaximumSize(QtCore.QSize(31, 31))
        self.otLightBulb2.setStyleSheet("QLabel { \n"
"color: #000000; \n"
"}")
        self.otLightBulb2.setText("")
        self.otLightBulb2.setPixmap(QtGui.QPixmap("icon/lights.png"))
        self.otLightBulb2.setScaledContents(True)
        self.otLightBulb2.setObjectName("otLightBulb2")
        self.gridLayout_2.addWidget(self.otLightBulb2, 0, 4, 1, 1)
        self.toggleContainerOT2 = QtWidgets.QWidget(Form)
        self.toggleContainerOT2.setMinimumSize(QtCore.QSize(111, 51))
        self.toggleContainerOT2.setMaximumSize(QtCore.QSize(111, 51))
        self.toggleContainerOT2.setObjectName("toggleContainerOT2")
        self.gridLayout_2.addWidget(self.toggleContainerOT2, 0, 5, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 5, 0, 1, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.light3Decrement = QtWidgets.QPushButton(Form)
        self.light3Decrement.setMinimumSize(QtCore.QSize(31, 31))
        self.light3Decrement.setMaximumSize(QtCore.QSize(31, 31))
        self.light3Decrement.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light3Decrement.setText("")
        self.light3Decrement.setIcon(icon)
        self.light3Decrement.setObjectName("light3Decrement")
        self.gridLayout_4.addWidget(self.light3Decrement, 0, 0, 1, 1)
        self.light3_1 = QtWidgets.QLabel(Form)
        self.light3_1.setMinimumSize(QtCore.QSize(8, 23))
        self.light3_1.setMaximumSize(QtCore.QSize(8, 23))
        self.light3_1.setStyleSheet("QLabel{\n"
" border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
" \n"
"  min-height: 15px;\n"
" \n"
" max-height: 15px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_1.setText("")
        self.light3_1.setObjectName("light3_1")
        self.gridLayout_4.addWidget(self.light3_1, 0, 1, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_2 = QtWidgets.QLabel(Form)
        self.light3_2.setMinimumSize(QtCore.QSize(8, 28))
        self.light3_2.setMaximumSize(QtCore.QSize(8, 28))
        self.light3_2.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 20px;\n"
" \n"
" max-height: 20px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_2.setText("")
        self.light3_2.setObjectName("light3_2")
        self.gridLayout_4.addWidget(self.light3_2, 0, 2, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_3 = QtWidgets.QLabel(Form)
        self.light3_3.setMinimumSize(QtCore.QSize(8, 33))
        self.light3_3.setMaximumSize(QtCore.QSize(8, 33))
        self.light3_3.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 25px;\n"
" \n"
" max-height: 25px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_3.setText("")
        self.light3_3.setObjectName("light3_3")
        self.gridLayout_4.addWidget(self.light3_3, 0, 3, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_4 = QtWidgets.QLabel(Form)
        self.light3_4.setMinimumSize(QtCore.QSize(8, 38))
        self.light3_4.setMaximumSize(QtCore.QSize(8, 38))
        self.light3_4.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 30px;\n"
" \n"
" max-height:30px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_4.setText("")
        self.light3_4.setObjectName("light3_4")
        self.gridLayout_4.addWidget(self.light3_4, 0, 4, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_5 = QtWidgets.QLabel(Form)
        self.light3_5.setMinimumSize(QtCore.QSize(8, 43))
        self.light3_5.setMaximumSize(QtCore.QSize(8, 43))
        self.light3_5.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 35px;\n"
" \n"
" max-height:35px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_5.setText("")
        self.light3_5.setObjectName("light3_5")
        self.gridLayout_4.addWidget(self.light3_5, 0, 5, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_6 = QtWidgets.QLabel(Form)
        self.light3_6.setMinimumSize(QtCore.QSize(8, 48))
        self.light3_6.setMaximumSize(QtCore.QSize(8, 48))
        self.light3_6.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 40px;\n"
" \n"
" max-height:40px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_6.setText("")
        self.light3_6.setObjectName("light3_6")
        self.gridLayout_4.addWidget(self.light3_6, 0, 6, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_7 = QtWidgets.QLabel(Form)
        self.light3_7.setMinimumSize(QtCore.QSize(8, 53))
        self.light3_7.setMaximumSize(QtCore.QSize(8, 53))
        self.light3_7.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 45px;\n"
" \n"
" max-height:45px;\n"
"   \n"
"  background-color:black;\n"
"}")
        self.light3_7.setText("")
        self.light3_7.setObjectName("light3_7")
        self.gridLayout_4.addWidget(self.light3_7, 0, 7, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_8 = QtWidgets.QLabel(Form)
        self.light3_8.setMinimumSize(QtCore.QSize(8, 58))
        self.light3_8.setMaximumSize(QtCore.QSize(8, 58))
        self.light3_8.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 50px;\n"
" \n"
"  max-height:50px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_8.setText("")
        self.light3_8.setObjectName("light3_8")
        self.gridLayout_4.addWidget(self.light3_8, 0, 8, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_9 = QtWidgets.QLabel(Form)
        self.light3_9.setMinimumSize(QtCore.QSize(8, 63))
        self.light3_9.setMaximumSize(QtCore.QSize(8, 63))
        self.light3_9.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 55px;\n"
" \n"
" max-height:55px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_9.setText("")
        self.light3_9.setObjectName("light3_9")
        self.gridLayout_4.addWidget(self.light3_9, 0, 9, 1, 1, QtCore.Qt.AlignBottom)
        self.light3_10 = QtWidgets.QLabel(Form)
        self.light3_10.setMinimumSize(QtCore.QSize(8, 68))
        self.light3_10.setMaximumSize(QtCore.QSize(8, 68))
        self.light3_10.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 60px;\n"
" \n"
" max-height:60px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light3_10.setText("")
        self.light3_10.setObjectName("light3_10")
        self.gridLayout_4.addWidget(self.light3_10, 0, 10, 1, 1, QtCore.Qt.AlignBottom)
        self.light3Increment = QtWidgets.QPushButton(Form)
        self.light3Increment.setMinimumSize(QtCore.QSize(31, 31))
        self.light3Increment.setMaximumSize(QtCore.QSize(31, 31))
        self.light3Increment.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light3Increment.setText("")
        self.light3Increment.setIcon(icon1)
        self.light3Increment.setObjectName("light3Increment")
        self.gridLayout_4.addWidget(self.light3Increment, 0, 11, 1, 1)
        self.light4Decrement = QtWidgets.QPushButton(Form)
        self.light4Decrement.setMinimumSize(QtCore.QSize(31, 31))
        self.light4Decrement.setMaximumSize(QtCore.QSize(31, 31))
        self.light4Decrement.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light4Decrement.setText("")
        self.light4Decrement.setIcon(icon)
        self.light4Decrement.setObjectName("light4Decrement")
        self.gridLayout_4.addWidget(self.light4Decrement, 0, 12, 1, 1)
        self.light4_1 = QtWidgets.QLabel(Form)
        self.light4_1.setMinimumSize(QtCore.QSize(8, 23))
        self.light4_1.setMaximumSize(QtCore.QSize(8, 23))
        self.light4_1.setStyleSheet("QLabel{\n"
" border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
" \n"
"  min-height: 15px;\n"
" \n"
" max-height: 15px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_1.setText("")
        self.light4_1.setObjectName("light4_1")
        self.gridLayout_4.addWidget(self.light4_1, 0, 13, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_2 = QtWidgets.QLabel(Form)
        self.light4_2.setMinimumSize(QtCore.QSize(8, 28))
        self.light4_2.setMaximumSize(QtCore.QSize(8, 28))
        self.light4_2.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 20px;\n"
" \n"
" max-height: 20px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_2.setText("")
        self.light4_2.setObjectName("light4_2")
        self.gridLayout_4.addWidget(self.light4_2, 0, 14, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_3 = QtWidgets.QLabel(Form)
        self.light4_3.setMinimumSize(QtCore.QSize(8, 33))
        self.light4_3.setMaximumSize(QtCore.QSize(8, 33))
        self.light4_3.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 25px;\n"
" \n"
" max-height: 25px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_3.setText("")
        self.light4_3.setObjectName("light4_3")
        self.gridLayout_4.addWidget(self.light4_3, 0, 15, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_4 = QtWidgets.QLabel(Form)
        self.light4_4.setMinimumSize(QtCore.QSize(8, 38))
        self.light4_4.setMaximumSize(QtCore.QSize(8, 38))
        self.light4_4.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 30px;\n"
" \n"
" max-height:30px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_4.setText("")
        self.light4_4.setObjectName("light4_4")
        self.gridLayout_4.addWidget(self.light4_4, 0, 16, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_5 = QtWidgets.QLabel(Form)
        self.light4_5.setMinimumSize(QtCore.QSize(8, 43))
        self.light4_5.setMaximumSize(QtCore.QSize(8, 43))
        self.light4_5.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"    padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 35px;\n"
" \n"
" max-height:35px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_5.setText("")
        self.light4_5.setObjectName("light4_5")
        self.gridLayout_4.addWidget(self.light4_5, 0, 17, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_6 = QtWidgets.QLabel(Form)
        self.light4_6.setMinimumSize(QtCore.QSize(8, 48))
        self.light4_6.setMaximumSize(QtCore.QSize(8, 48))
        self.light4_6.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 40px;\n"
" \n"
" max-height:40px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_6.setText("")
        self.light4_6.setObjectName("light4_6")
        self.gridLayout_4.addWidget(self.light4_6, 0, 18, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_7 = QtWidgets.QLabel(Form)
        self.light4_7.setMinimumSize(QtCore.QSize(8, 53))
        self.light4_7.setMaximumSize(QtCore.QSize(8, 53))
        self.light4_7.setStyleSheet("QLabel{\n"
"   border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 45px;\n"
" \n"
" max-height:45px;\n"
"   \n"
"  background-color:black;\n"
"}")
        self.light4_7.setText("")
        self.light4_7.setObjectName("light4_7")
        self.gridLayout_4.addWidget(self.light4_7, 0, 19, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_8 = QtWidgets.QLabel(Form)
        self.light4_8.setMinimumSize(QtCore.QSize(8, 58))
        self.light4_8.setMaximumSize(QtCore.QSize(8, 58))
        self.light4_8.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"   padding:2px;  \n"
"    border-radius:4px;\n"
"  border-width: 2px;\n"
"  min-height: 50px;\n"
" \n"
"  max-height:50px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_8.setText("")
        self.light4_8.setObjectName("light4_8")
        self.gridLayout_4.addWidget(self.light4_8, 0, 20, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_9 = QtWidgets.QLabel(Form)
        self.light4_9.setMinimumSize(QtCore.QSize(8, 63))
        self.light4_9.setMaximumSize(QtCore.QSize(8, 63))
        self.light4_9.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 55px;\n"
" \n"
" max-height:55px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_9.setText("")
        self.light4_9.setObjectName("light4_9")
        self.gridLayout_4.addWidget(self.light4_9, 0, 21, 1, 1, QtCore.Qt.AlignBottom)
        self.light4_10 = QtWidgets.QLabel(Form)
        self.light4_10.setMinimumSize(QtCore.QSize(8, 68))
        self.light4_10.setMaximumSize(QtCore.QSize(8, 68))
        self.light4_10.setStyleSheet("QLabel{\n"
"  border-style: outset;\n"
"  padding:2px;  \n"
"    border-radius:4px;\n"
"    \n"
"   border-width: 2px;\n"
"  min-height: 60px;\n"
" \n"
" max-height:60px;\n"
" \n"
"  background-color:black;\n"
"}")
        self.light4_10.setText("")
        self.light4_10.setObjectName("light4_10")
        self.gridLayout_4.addWidget(self.light4_10, 0, 22, 1, 1, QtCore.Qt.AlignBottom)
        self.light4Increment = QtWidgets.QPushButton(Form)
        self.light4Increment.setMinimumSize(QtCore.QSize(31, 31))
        self.light4Increment.setMaximumSize(QtCore.QSize(31, 31))
        self.light4Increment.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px; \n"
"    padding: 6px;\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.light4Increment.setText("")
        self.light4Increment.setIcon(icon1)
        self.light4Increment.setObjectName("light4Increment")
        self.gridLayout_4.addWidget(self.light4Increment, 0, 23, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 6, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setMinimumSize(QtCore.QSize(581, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 7, 0, 1, 3)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lightLabel1.setText(_translate("Form", "Gen Light - 1"))
        self.lightLabel2.setText(_translate("Form", "Gen Light - 2"))
        self.lightLabel3.setText(_translate("Form", "OT 1"))
        self.lightLabel4.setText(_translate("Form", "Peripheral"))
        self.lightLabel5.setText(_translate("Form", "Laminar"))
        self.lightLabel6.setText(_translate("Form", "OT 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

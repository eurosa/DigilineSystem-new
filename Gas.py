# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gas.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(578, 254)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gasLabel_1_high = QtWidgets.QLabel(Form)
        self.gasLabel_1_high.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_1_high.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_1_high.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_1_high.setObjectName("gasLabel_1_high")
        self.verticalLayout_12.addWidget(self.gasLabel_1_high)
        self.gasLabel_1_normal = QtWidgets.QLabel(Form)
        self.gasLabel_1_normal.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_1_normal.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_1_normal.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_1_normal.setObjectName("gasLabel_1_normal")
        self.verticalLayout_12.addWidget(self.gasLabel_1_normal)
        self.gasLabel_1_low = QtWidgets.QLabel(Form)
        self.gasLabel_1_low.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_1_low.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_1_low.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_1_low.setObjectName("gasLabel_1_low")
        self.verticalLayout_12.addWidget(self.gasLabel_1_low)
        self.gridLayout_2.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gasLabel_5_high = QtWidgets.QLabel(Form)
        self.gasLabel_5_high.setMaximumSize(QtCore.QSize(110, 32))
        self.gasLabel_5_high.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_5_high.setObjectName("gasLabel_5_high")
        self.verticalLayout_3.addWidget(self.gasLabel_5_high)
        self.gasLabel_5_normal = QtWidgets.QLabel(Form)
        self.gasLabel_5_normal.setMaximumSize(QtCore.QSize(110, 32))
        self.gasLabel_5_normal.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_5_normal.setObjectName("gasLabel_5_normal")
        self.verticalLayout_3.addWidget(self.gasLabel_5_normal)
        self.gasLabel_5_low = QtWidgets.QLabel(Form)
        self.gasLabel_5_low.setMaximumSize(QtCore.QSize(110, 32))
        self.gasLabel_5_low.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_5_low.setObjectName("gasLabel_5_low")
        self.verticalLayout_3.addWidget(self.gasLabel_5_low)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 4, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gasLabel_2_high = QtWidgets.QLabel(Form)
        self.gasLabel_2_high.setMaximumSize(QtCore.QSize(110, 32))
        self.gasLabel_2_high.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_2_high.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_2_high.setObjectName("gasLabel_2_high")
        self.verticalLayout_6.addWidget(self.gasLabel_2_high)
        self.gasLabel_2_normal = QtWidgets.QLabel(Form)
        self.gasLabel_2_normal.setMaximumSize(QtCore.QSize(110, 32))
        self.gasLabel_2_normal.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_2_normal.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_2_normal.setObjectName("gasLabel_2_normal")
        self.verticalLayout_6.addWidget(self.gasLabel_2_normal)
        self.gasLabel_2_low = QtWidgets.QLabel(Form)
        self.gasLabel_2_low.setMaximumSize(QtCore.QSize(110, 32))
        self.gasLabel_2_low.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_2_low.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_2_low.setObjectName("gasLabel_2_low")
        self.verticalLayout_6.addWidget(self.gasLabel_2_low)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gasLabel_3_high = QtWidgets.QLabel(Form)
        self.gasLabel_3_high.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_3_high.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_3_high.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_3_high.setObjectName("gasLabel_3_high")
        self.verticalLayout.addWidget(self.gasLabel_3_high)
        self.gasLabel_3_normal = QtWidgets.QLabel(Form)
        self.gasLabel_3_normal.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_3_normal.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_3_normal.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_3_normal.setObjectName("gasLabel_3_normal")
        self.verticalLayout.addWidget(self.gasLabel_3_normal)
        self.gasLabel_3_low = QtWidgets.QLabel(Form)
        self.gasLabel_3_low.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_3_low.setSizeIncrement(QtCore.QSize(51, 0))
        self.gasLabel_3_low.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_3_low.setObjectName("gasLabel_3_low")
        self.verticalLayout.addWidget(self.gasLabel_3_low)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gasLabel_4_high = QtWidgets.QLabel(Form)
        self.gasLabel_4_high.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_4_high.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_4_high.setObjectName("gasLabel_4_high")
        self.verticalLayout_2.addWidget(self.gasLabel_4_high)
        self.gasLabel_4_normal = QtWidgets.QLabel(Form)
        self.gasLabel_4_normal.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_4_normal.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_4_normal.setObjectName("gasLabel_4_normal")
        self.verticalLayout_2.addWidget(self.gasLabel_4_normal)
        self.gasLabel_4_low = QtWidgets.QLabel(Form)
        self.gasLabel_4_low.setMaximumSize(QtCore.QSize(111, 32))
        self.gasLabel_4_low.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_4_low.setObjectName("gasLabel_4_low")
        self.verticalLayout_2.addWidget(self.gasLabel_4_low)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gasLabel_6_normal = QtWidgets.QLabel(Form)
        self.gasLabel_6_normal.setMaximumSize(QtCore.QSize(111, 51))
        self.gasLabel_6_normal.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_6_normal.setObjectName("gasLabel_6_normal")
        self.verticalLayout_4.addWidget(self.gasLabel_6_normal)
        self.gasLabel_6_low = QtWidgets.QLabel(Form)
        self.gasLabel_6_low.setMaximumSize(QtCore.QSize(111, 51))
        self.gasLabel_6_low.setStyleSheet("QLabel { \n"
"    text-align: center;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 4em;\n"
"    padding: 6px;\n"
"    color:#FFFFFF;\n"
"   background-color:#000000;\n"
"}")
        self.gasLabel_6_low.setObjectName("gasLabel_6_low")
        self.verticalLayout_4.addWidget(self.gasLabel_6_low)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 5, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gasLabel_6 = QtWidgets.QLabel(Form)
        self.gasLabel_6.setMaximumSize(QtCore.QSize(113, 50))
        self.gasLabel_6.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.gasLabel_6.setObjectName("gasLabel_6")
        self.gridLayout_4.addWidget(self.gasLabel_6, 1, 5, 1, 1, QtCore.Qt.AlignTop)
        self.gasLabel_5 = QtWidgets.QLabel(Form)
        self.gasLabel_5.setMaximumSize(QtCore.QSize(112, 50))
        self.gasLabel_5.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.gasLabel_5.setObjectName("gasLabel_5")
        self.gridLayout_4.addWidget(self.gasLabel_5, 1, 4, 1, 1, QtCore.Qt.AlignTop)
        self.gasLabel_3 = QtWidgets.QLabel(Form)
        self.gasLabel_3.setMaximumSize(QtCore.QSize(113, 50))
        self.gasLabel_3.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.gasLabel_3.setObjectName("gasLabel_3")
        self.gridLayout_4.addWidget(self.gasLabel_3, 1, 2, 1, 1, QtCore.Qt.AlignTop)
        self.gasLabel_4 = QtWidgets.QLabel(Form)
        self.gasLabel_4.setMaximumSize(QtCore.QSize(113, 50))
        self.gasLabel_4.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.gasLabel_4.setObjectName("gasLabel_4")
        self.gridLayout_4.addWidget(self.gasLabel_4, 1, 3, 1, 1, QtCore.Qt.AlignTop)
        self.gasLabel_2 = QtWidgets.QLabel(Form)
        self.gasLabel_2.setMaximumSize(QtCore.QSize(112, 50))
        self.gasLabel_2.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.gasLabel_2.setObjectName("gasLabel_2")
        self.gridLayout_4.addWidget(self.gasLabel_2, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.gasLabel_1 = QtWidgets.QLabel(Form)
        self.gasLabel_1.setMaximumSize(QtCore.QSize(113, 50))
        self.gasLabel_1.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.gasLabel_1.setObjectName("gasLabel_1")
        self.gridLayout_4.addWidget(self.gasLabel_1, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gasLabel_1_high.setText(_translate("Form", "High"))
        self.gasLabel_1_normal.setText(_translate("Form", "Normal"))
        self.gasLabel_1_low.setText(_translate("Form", "Low"))
        self.gasLabel_5_high.setText(_translate("Form", "High"))
        self.gasLabel_5_normal.setText(_translate("Form", "Normal"))
        self.gasLabel_5_low.setText(_translate("Form", "Low"))
        self.gasLabel_2_high.setText(_translate("Form", "High"))
        self.gasLabel_2_normal.setText(_translate("Form", "Normal"))
        self.gasLabel_2_low.setText(_translate("Form", "Low"))
        self.gasLabel_3_high.setText(_translate("Form", "High"))
        self.gasLabel_3_normal.setText(_translate("Form", "Normal"))
        self.gasLabel_3_low.setText(_translate("Form", "Low"))
        self.gasLabel_4_high.setText(_translate("Form", "High"))
        self.gasLabel_4_normal.setText(_translate("Form", "Normal"))
        self.gasLabel_4_low.setText(_translate("Form", "Low"))
        self.gasLabel_6_normal.setText(_translate("Form", "Normal"))
        self.gasLabel_6_low.setText(_translate("Form", "Low"))
        self.gasLabel_6.setText(_translate("Form", "<html><head/><body><p align=\"center\">Vacuum</p></body></html>"))
        self.gasLabel_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">Carbon </p><p align=\"center\">Dioxide</p></body></html>"))
        self.gasLabel_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">Medical </p><p align=\"center\">Air</p></body></html>"))
        self.gasLabel_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Instrument </p><p align=\"center\">Air</p></body></html>"))
        self.gasLabel_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Nitrous </p><p align=\"center\">Oxide</p></body></html>"))
        self.gasLabel_1.setText(_translate("Form", "<html><head/><body><p align=\"center\">Oxygen</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

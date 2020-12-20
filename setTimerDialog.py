# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setTimerDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setTimer(object):
    def setupUi(self, setTimer):
        setTimer.setObjectName("setTimer")
        setTimer.resize(535, 340)
        setTimer.setStyleSheet(" QDialog{\n"
"background-color:#000000;\n"
"}")
        setTimer.setSizeGripEnabled(False)
        setTimer.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(setTimer)
        self.buttonBox.setGeometry(QtCore.QRect(270, 270, 211, 61))
        self.buttonBox.setStyleSheet("QDialogButtonBox{\n"
"color:#FFFFFF;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.hourSlider = QtWidgets.QSlider(setTimer)
        self.hourSlider.setGeometry(QtCore.QRect(120, 140, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.hourSlider.setFont(font)
        self.hourSlider.setStyleSheet("")
        self.hourSlider.setMaximum(99)
        self.hourSlider.setSingleStep(1)
        self.hourSlider.setProperty("value", 99)
        self.hourSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hourSlider.setObjectName("hourSlider")
        self.minuteSlider = QtWidgets.QSlider(setTimer)
        self.minuteSlider.setGeometry(QtCore.QRect(120, 190, 371, 51))
        self.minuteSlider.setStyleSheet("")
        self.minuteSlider.setMaximum(59)
        self.minuteSlider.setSingleStep(1)
        self.minuteSlider.setProperty("value", 59)
        self.minuteSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minuteSlider.setObjectName("minuteSlider")
        self.secondSlider = QtWidgets.QSlider(setTimer)
        self.secondSlider.setGeometry(QtCore.QRect(120, 240, 371, 51))
        self.secondSlider.setStyleSheet("")
        self.secondSlider.setMaximum(59)
        self.secondSlider.setSingleStep(1)
        self.secondSlider.setProperty("value", 59)
        self.secondSlider.setOrientation(QtCore.Qt.Horizontal)
        self.secondSlider.setObjectName("secondSlider")
        self.spinSecondBox = QtWidgets.QSpinBox(setTimer)
        self.spinSecondBox.setGeometry(QtCore.QRect(370, 30, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spinSecondBox.setFont(font)
        self.spinSecondBox.setStyleSheet("QSpinBox::up-button { width: 48px; }\n"
"QSpinBox::down-button { width: 48px; }\n"
"QSpinBox{\n"
"font:51px;\n"
"}\n"
"")
        self.spinSecondBox.setMaximum(59)
        self.spinSecondBox.setProperty("value", 59)
        self.spinSecondBox.setObjectName("spinSecondBox")
        self.spinMinuteBox = QtWidgets.QSpinBox(setTimer)
        self.spinMinuteBox.setGeometry(QtCore.QRect(210, 30, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(40)
        self.spinMinuteBox.setFont(font)
        self.spinMinuteBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinMinuteBox.setStyleSheet("QSpinBox::up-button { width: 48px; }\n"
"QSpinBox::down-button { width: 48px; }\n"
"")
        self.spinMinuteBox.setMaximum(59)
        self.spinMinuteBox.setProperty("value", 59)
        self.spinMinuteBox.setObjectName("spinMinuteBox")
        self.spinHourBox = QtWidgets.QSpinBox(setTimer)
        self.spinHourBox.setGeometry(QtCore.QRect(40, 30, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(36)
        self.spinHourBox.setFont(font)
        self.spinHourBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinHourBox.setStyleSheet("QSpinBox::up-button { width: 48px; }\n"
"QSpinBox::down-button { width: 48px; }\n"
" \n"
"")
        self.spinHourBox.setMaximum(99)
        self.spinHourBox.setProperty("value", 99)
        self.spinHourBox.setObjectName("spinHourBox")
        self.label_3 = QtWidgets.QLabel(setTimer)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 59, 28))
        self.label_3.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(setTimer)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 51, 45))
        self.label_2.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(setTimer)
        self.label.setGeometry(QtCore.QRect(50, 150, 41, 31))
        self.label.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(setTimer)
        self.label_4.setGeometry(QtCore.QRect(70, 0, 41, 31))
        self.label_4.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(setTimer)
        self.label_5.setGeometry(QtCore.QRect(250, 0, 51, 21))
        self.label_5.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(setTimer)
        self.label_6.setGeometry(QtCore.QRect(400, 0, 59, 21))
        self.label_6.setStyleSheet("QLabel{\n"
"color:#FFFFFF;\n"
"}")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(setTimer)
        self.buttonBox.accepted.connect(setTimer.accept)
        self.buttonBox.rejected.connect(setTimer.reject)
        QtCore.QMetaObject.connectSlotsByName(setTimer)

    def retranslateUi(self, setTimer):
        _translate = QtCore.QCoreApplication.translate
        setTimer.setWindowTitle(_translate("setTimer", "Timer Setting"))
        self.label_3.setText(_translate("setTimer", "Second"))
        self.label_2.setText(_translate("setTimer", "Minute"))
        self.label.setText(_translate("setTimer", "Hour"))
        self.label_4.setText(_translate("setTimer", "Hour"))
        self.label_5.setText(_translate("setTimer", "Minute"))
        self.label_6.setText(_translate("setTimer", "Second"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setTimer = QtWidgets.QDialog()
    ui = Ui_setTimer()
    ui.setupUi(setTimer)
    setTimer.show()
    sys.exit(app.exec_())

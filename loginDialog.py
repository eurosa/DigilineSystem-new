# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(317, 129)
        self.gridLayout_2 = QtWidgets.QGridLayout(loginDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelUserName = QtWidgets.QLabel(loginDialog)
        self.labelUserName.setMinimumSize(QtCore.QSize(79, 33))
        self.labelUserName.setObjectName("labelUserName")
        self.gridLayout.addWidget(self.labelUserName, 0, 0, 1, 1)
        self.user_name = QtWidgets.QLineEdit(loginDialog)
        self.user_name.setMinimumSize(QtCore.QSize(212, 33))
        self.user_name.setObjectName("user_name")
        self.gridLayout.addWidget(self.user_name, 0, 1, 1, 1)
        self.labelUserPass = QtWidgets.QLabel(loginDialog)
        self.labelUserPass.setMinimumSize(QtCore.QSize(79, 33))
        self.labelUserPass.setObjectName("labelUserPass")
        self.gridLayout.addWidget(self.labelUserPass, 1, 0, 1, 1)
        self.user_pass = QtWidgets.QLineEdit(loginDialog)
        self.user_pass.setMinimumSize(QtCore.QSize(212, 33))
        self.user_pass.setObjectName("user_pass")
        self.gridLayout.addWidget(self.user_pass, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.loginButton = QtWidgets.QPushButton(loginDialog)
        self.loginButton.setMinimumSize(QtCore.QSize(299, 31))
        self.loginButton.setObjectName("loginButton")
        self.gridLayout_2.addWidget(self.loginButton, 1, 0, 1, 1)

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        _translate = QtCore.QCoreApplication.translate
        loginDialog.setWindowTitle(_translate("loginDialog", "Login Form"))
        self.labelUserName.setText(_translate("loginDialog", "User Name:"))
        self.labelUserPass.setText(_translate("loginDialog", "Password:"))
        self.loginButton.setText(_translate("loginDialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginDialog = QtWidgets.QDialog()
    ui = Ui_loginDialog()
    ui.setupUi(loginDialog)
    loginDialog.show()
    sys.exit(app.exec_())

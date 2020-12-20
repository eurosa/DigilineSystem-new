from PyQt5 import QtCore, QtGui, QtWidgets


class PushButtonColorControl:
    def __init__(self, pushButton_ui):
        self.pushButton_ui = pushButton_ui
        self.change_image()

    def change_image(self, color=QtGui.QColor("white")):
        n_color = QtGui.QColor(color)
        print(str(n_color.name()))
        self.pushButton_ui.setStyleSheet("QPushButton {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"     \n"
"    padding: 6px;\n"
"    background-color: "+n_color.name()+";\n"
"    color:#FFFFFF;\n"
"   \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: gray;\n"
"    border-style: inset;\n"
"}\n"
"")
        # self.settingsDialog_ui.borderColor

    def processButton_DMX(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.white)
        if color.isValid():
            self.change_image(color)

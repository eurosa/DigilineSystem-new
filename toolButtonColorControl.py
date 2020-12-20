import os
import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from Database import database
from Database.dataModel import DataModel

dir_path = os.path.dirname(os.path.realpath(__file__))


class ToolButtonColorControl:
    def __init__(self, toolButton_ui, model, changer_name):
        self.toolButton_ui = toolButton_ui
        self.datamodel = model
        self.changer_name = changer_name
        self.database_manage = database.DataBaseManagement()
        path_image = os.path.join(dir_path, "icon/fan_white.png").replace("\\", "/")
        # self.image = QtGui.QImage(path_image)
        self.image = QtGui.QImage(self.toolButton_ui.icon().pixmap(self.toolButton_ui.iconSize()))
        # self.change_image()
        # self.default_color_database(self.model)

    def change_image(self, color=QtGui.QColor("white")):
        n_color = QtGui.QColor(color)
        if self.changer_name == 'border_color':
            self.datamodel.set_border_col(n_color.name())
            print("My border_color: " + n_color.name())
        elif self.changer_name == 'text_color':
            print("My text_color: " + n_color.name())
            self.datamodel.set_text_col(n_color.name())
        elif self.changer_name == 'background_color':
            print("My background_color: " + n_color.name())
            self.datamodel.set_background_col(n_color.name())
        elif self.changer_name == 'icon_color':
            for x in range(self.image.width()):
                for y in range(self.image.height()):
                    pcolor = self.image.pixelColor(x, y)
                    if pcolor.alpha() > 0:
                        n_color = QtGui.QColor(color)
                        n_color.setAlpha(pcolor.alpha())
                        self.image.setPixelColor(x, y, n_color)
            print("My icon_color: " + str(QtGui.QColor(n_color.name())))
            print("My icon_color_hex: " + str(QtGui.QColor(n_color.name()).name()))
            print("My icon_color_absolute_hex: " + n_color.name())
            self.datamodel.set_icon_col(n_color.name())
            self.toolButton_ui.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.image)))
            self.toolButton_ui.setIconSize(QtCore.QSize(31, 31))

        if self.changer_name == 'border_color':
            self.toolButton_ui.setStyleSheet("QToolButton {\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: " + self.datamodel.get_border_col() + ";\n"
                                             "    font: bold 14px;\n"
                                             "     \n"
                                             "    padding: 6px;\n"
                                             "    background-color: " + self.datamodel.get_border_col() + ";\n"
                                                                                                          "    color:#FFFFFF;\n"
                                                                                                          "   \n"
                                                                                                          "}\n"
                                                                                                          "QToolButton:pressed {\n"
                                                                                                          "    background-color: gray;\n"
                                                                                                          "    border-style: inset;\n"
                                                                                                          "}\n"
                                                                                                          "")
        elif self.changer_name == 'background_color':
            self.toolButton_ui.setStyleSheet("QToolButton {\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: " + self.datamodel.get_border_col() + ";\n"
                                             "    font: bold 14px;\n"
                                             "     \n"
                                             "    padding: 6px;\n"
                                             "    background-color: " + self.datamodel.get_background_col() + ";\n"
                                                                                                              "    color:#FFFFFF;\n"
                                                                                                              "   \n"
                                                                                                              "}\n"
                                                                                                              "QToolButton:pressed {\n"
                                                                                                              "    background-color: gray;\n"
                                                                                                              "    border-style: inset;\n"
                                                                                                              "}\n"
                                                                                                              "")
        elif self.changer_name == 'text_color':
            self.toolButton_ui.setStyleSheet("QToolButton {\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: " + self.datamodel.get_border_col() + ";\n"
                                             "    font: bold 14px;\n"
                                             "     \n"
                                             "    padding: 6px;\n"
                                             "    background-color: " + self.datamodel.get_text_col() + ";\n"
                                                                                                        "    color:#FFFFFF;\n"
                                                                                                        "   \n"
                                                                                                        "}\n"
                                                                                                        "QToolButton:pressed {\n"
                                                                                                        "    background-color: gray;\n"
                                                                                                        "    border-style: inset;\n"
                                                                                                        "}\n"
                                                                                                        "")
        elif self.changer_name == 'icon_color':
            print("Tool Icon:" + self.datamodel.get_icon_col())
            for x in range(self.image.width()):
                for y in range(self.image.height()):
                    pcolor = self.image.pixelColor(x, y)
                    if pcolor.alpha() > 0:
                        n_color = QtGui.QColor(self.datamodel.get_icon_col())
                        n_color.setAlpha(pcolor.alpha())
                        self.image.setPixelColor(x, y, n_color)
            self.toolButton_ui.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.image)))
            self.toolButton_ui.setIconSize(QtCore.QSize(31, 31))

        # self.model = DataModel()
        # self.database_manage.queryIconColorSettings(self.model)
        # self.default_color_database()

    # self.settingsDialog_ui.borderColor
    def default_color_database(self, model):
        self.datamod = model
        # print(str(n_color.name()))
        if self.changer_name == 'border_color':
            self.toolButton_ui.setStyleSheet("QToolButton {\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: " + self.datamod.get_border_col() + ";\n"
                                             "    font: bold 14px;\n"
                                             "     \n"
                                             "    padding: 6px;\n"
                                             "    background-color: " + self.datamod.get_border_col() + ";\n"
                                                                                                        "    color:#FFFFFF;\n"
                                                                                                        "   \n"
                                                                                                        "}\n"
                                                                                                        "QToolButton:pressed {\n"
                                                                                                        "    background-color: gray;\n"
                                                                                                        "    border-style: inset;\n"
                                                                                                        "}\n"
                                                                                                        "")
        elif self.changer_name == 'background_color':
            self.toolButton_ui.setStyleSheet("QToolButton {\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: " + self.datamod.get_border_col() + ";\n"
                                             "    font: bold 14px;\n"
                                             "     \n"
                                             "    padding: 6px;\n"
                                             "    background-color: " + self.datamod.get_background_col() + ";\n"
                                                                                                            "    color:#FFFFFF;\n"
                                                                                                            "   \n"
                                                                                                            "}\n"
                                                                                                            "QToolButton:pressed {\n"
                                                                                                            "    background-color: gray;\n"
                                                                                                            "    border-style: inset;\n"
                                                                                                            "}\n"
                                                                                                            "")
        elif self.changer_name == 'text_color':
            self.toolButton_ui.setStyleSheet("QToolButton {\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color: " + self.datamod.get_border_col() + ";\n"
                                             "    font: bold 14px;\n"
                                             "     \n"
                                             "    padding: 6px;\n"
                                             "    background-color: " + self.datamod.get_text_col() + ";\n"
                                                                                                      "    color:#FFFFFF;\n"
                                                                                                      "   \n"
                                                                                                      "}\n"
                                                                                                      "QToolButton:pressed {\n"
                                                                                                      "    background-color: gray;\n"
                                                                                                      "    border-style: inset;\n"
                                                                                                      "}\n"
                                                                                                      "")
        elif self.changer_name == 'icon_color':
            print("Tool Icon:" + self.datamodel.get_icon_col())
            for x in range(self.image.width()):
                for y in range(self.image.height()):
                    pcolor = self.image.pixelColor(x, y)
                    if pcolor.alpha() > 0:
                        n_color = QtGui.QColor(self.datamodel.get_icon_col())
                        n_color.setAlpha(pcolor.alpha())
                        self.image.setPixelColor(x, y, n_color)
            self.toolButton_ui.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.image)))
            self.toolButton_ui.setIconSize(QtCore.QSize(31, 31))

    def processButton_DMX(self):
        colorDialog = QtWidgets.QColorDialog()
        color = colorDialog.getColor(QtCore.Qt.white)
        if color.isValid():
            self.change_image(color)

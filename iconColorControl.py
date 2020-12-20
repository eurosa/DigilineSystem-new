import os
import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

dir_path = os.path.dirname(os.path.realpath(__file__))


class IconColorControl:
    def __init__(self, settingsDialog_ui, model, changer_name):
        self.settingsDialog_ui = settingsDialog_ui
        self.model = model
        self.changer_name = changer_name
        path_image = os.path.join(dir_path, "icon/fan_white.png").replace("\\", "/")
        self.image = QtGui.QImage(path_image)
        # self.settingsDialog_ui.iconColor.clicked.connect(self.processButton_DMX)
        self.change_image()

    def change_image(self, color=QtGui.QColor("white")):
        for x in range(self.image.width()):
            for y in range(self.image.height()):
                pcolor = self.image.pixelColor(x, y)
                if pcolor.alpha() > 0:
                    n_color = QtGui.QColor(color)
                    n_color.setAlpha(pcolor.alpha())
                    self.image.setPixelColor(x, y, n_color)
        if self.changer_name == 'icon_color':
            self.model.set_icon_color(n_color.name())
        self.settingsDialog_ui.iconColor.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.image)))
        self.settingsDialog_ui.iconColor.setIconSize(QtCore.QSize(31, 31))
        # self.button_DMX.setIconSize(self.image.size())
        # self.button_DMX.setFixedSize(self.image.size())

    def processButton_DMX(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.white)
        if color.isValid():
            self.change_image(color)


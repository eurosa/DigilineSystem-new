import time

from PyQt5.QtCore import pyqtSlot, QRunnable, QObject, pyqtSignal

import configVariables
from Database import switchdatabase


class Signals(QObject):
    return_signal = pyqtSignal(str)


class GraphThread(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(GraphThread, self).__init__()
        self.signal = Signals()
        self.ui = ui
        # =========+Alarm History Details Database Manage+=============================================

    @pyqtSlot()
    def run(self):
        # time.sleep(5)
        result = "RXTX"
        while True:
            self.signal.return_signal.emit(result)
            # self.ui.drawRealTimeData()
            time.sleep(1)
        # ------------------------------------------------------
        # self.ui.settings_dialog_set_ui.labelDisplayTheme.setPixmap(QtGui.QPixmap(self.ui.dataModel.get_theme_color_preview()))
        # self.ui.alldisplayColorChangeObj.changeSettingsDialogAttributeColor(self.ui.SettingsQDialog)
        # self.signal.return_signal.emit(result)

    def function_thread(self, signal):
        pass
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj) self.threadpool.destroyed() Index out
        # of range error if configVariables.hex_string[0] == 0x2 and configVariables.hex_string[1] == 0x31 \ in
        # rasberry pi
        # Aborted in rasberry pi
        # print(configVariables.hex_string)
        # print(signal)

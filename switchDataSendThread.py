from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, QTimer

import configVariables


class Signals(QObject):
    return_signal = pyqtSignal(str)


class ThreadDataSwitchData(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(ThreadDataSwitchData, self).__init__()
        self.signal = Signals()
        self.ui = ui

    def run(self):
        # time.sleep(5)
        result = "Some String"
        # ======================= Login UI ==========================================================================
        self.ui.hexAdd("0x8")
        # setting background color to light-blue
        configVariables.totalHex = "0x46"
        self.ui.serialWrapper.sendDataToSerialPort(int(configVariables.totalHex, 16))
        self.ui.toggleSwitch.setStyleSheet("background-color : #FFFFFF")
        self.ui.ot_ui.lightBulb3.setPixmap(configVariables.changed_light_bulb)

        self.signal.return_signal.emit(result)

    def function_thread(self, signal):
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        # self.threadpool.destroyed()
        print("My Goodness")
        print(signal)

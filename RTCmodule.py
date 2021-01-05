import os
import subprocess
from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, QTimer
import time

from main import Thread


class Signals(QObject):
    return_signal = pyqtSignal(str)


class RTCThread(QRunnable):
    signal = pyqtSignal(str)

    def __init__(self, ui):
        super(RTCThread, self).__init__()
        self.signal = Signals()
        self.ui = ui
        self.result = ''

    def run(self):
        # time.sleep(5)
        self.result = "Some String"
        while True:
            os.system("sudo hwclock -r")
            self.result = subprocess.call(
               'echo vishnu | sudo hwclock -r', shell=True)
            # srt = os.system('hwclock -r')
            self.ui.ui.day_date_show.setText(self.result)
            time.sleep(1)

        self.signal.return_signal.emit(self.result)

    def function_thread(self, signal):
        # QTimer.singleShot(2000, lambda: self.settings_dialog_set_ui.applyColor.setDisabled(False))
        # self.allChangeToolButtonAttributeColor(self.alldisplayColorChangeObj)
        # self.threadpool.destroyed()
        print(signal)



